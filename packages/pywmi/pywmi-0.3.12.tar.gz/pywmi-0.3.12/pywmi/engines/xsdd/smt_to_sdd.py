from typing import Type

from pywmi.engines.algebraic_backend import AlgebraBackend
from pywmi.engines.xsdd.piecewise import PiecewiseXSDD
from .semiring import Semiring, amc
from pywmi.smt_math import get_inequality_smt

try:
    from pysdd.sdd import SddManager, SddNode
except ImportError:
    SddManager = None
    SddNode = None

from pysmt.fnode import FNode
from pysmt.shortcuts import Symbol, Pow, TRUE, FALSE, simplify
from pysmt.typing import REAL, BOOL
from pywmi import SmtWalker
from pywmi.errors import InstallError


def product(*elements):
    result = elements[0]
    for e in elements[1:]:
        result *= e
    return result


class SddConversionWalker(SmtWalker):
    def __init__(self, manager, algebra: Type[AlgebraBackend], boolean_only, abstractions=None, var_to_lit=None):
        self.manager = manager  # type: SddManager
        self.algebra = algebra
        self.abstractions = abstractions if abstractions is not None else dict()
        self.var_to_lit = var_to_lit if var_to_lit is not None else dict()
        self.boolean_stack = [boolean_only]

    def new_literal(self):
        literal = self.manager.var_count() + 1
        self.manager.add_var_after_last()
        return literal

    def to_canonical(self, test_node):
        return get_inequality_smt(test_node)

    def test_to_sdd(self, test_node):
        test_node = self.to_canonical(test_node)
        negate = False
        if test_node.arg(1).constant_value() == -1:
            test_node = self.to_canonical(test_node.arg(0) >= test_node.arg(1))
            negate = True
        # node_id = test_node.node_id()
        if test_node not in self.abstractions:
            literal = self.new_literal()
            self.abstractions[test_node] = literal
        result = self.manager.l(self.abstractions[test_node])
        if negate:
            result = result.negate()
        return result

    def walk_and(self, args):
        if not self.boolean_stack[-1]:
            raise ValueError("Parsing mode must be boolean")
        converted = self.walk_smt_multiple(args)

        result = converted[0]
        for term in converted[1:]:
            result = self.manager.conjoin(result, term)
        return result

    def walk_or(self, args):
        if not self.boolean_stack[-1]:
            raise ValueError("Parsing mode must be boolean")
        converted = self.walk_smt_multiple(args)

        result = converted[0]
        for term in converted[1:]:
            result = self.manager.disjoin(result, term)
        return result

    def walk_plus(self, args):
        if self.boolean_stack[-1]:
            raise ValueError("Parsing mode must be non-boolean")
        converted = self.walk_smt_multiple(args)

        result = converted[0]
        for c in converted[1:]:
            result += c
        return result

    def walk_minus(self, left, right):
        if self.boolean_stack[-1]:
            raise ValueError("Parsing mode must be non-boolean")

        left, right = self.walk_smt_multiple([left, right])

        return left + (~right)

    def walk_times(self, args):
        if self.boolean_stack[-1]:
            raise ValueError("Parsing mode must be non-boolean")
        converted = self.walk_smt_multiple(args)

        result = converted[0]
        for c in converted[1:]:
            result *= c
        return result

    def walk_not(self, argument):
        if not self.boolean_stack[-1]:
            raise ValueError("Parsing mode must be boolean")

        return self.manager.negate(self.walk_smt(argument))

    def walk_ite(self, if_arg, then_arg, else_arg):
        if self.boolean_stack[-1]:
            return self.walk_smt((if_arg & then_arg) | (~if_arg & else_arg))

        self.boolean_stack.append(True)
        sdd = self.walk_smt(if_arg)
        self.boolean_stack[-1] = False
        then_expression, else_expression = self.walk_smt_multiple([then_arg, else_arg])
        self.boolean_stack.pop()

        return PiecewiseXSDD.ite(sdd, then_expression, else_expression)

    def walk_pow(self, base, exponent):
        return Pow(base, exponent)

    def walk_lte(self, left: FNode, right: FNode):
        if not self.boolean_stack[-1]:
            raise ValueError("Parsing mode must be boolean")

        return self.test_to_sdd(left <= right)

    def walk_lt(self, left: FNode, right: FNode):
        if not self.boolean_stack[-1]:
            raise ValueError("Parsing mode must be boolean")

        return self.test_to_sdd(left < right)

    def walk_equals(self, left, right):
        raise RuntimeError("Not supported")

    def walk_symbol(self, name, v_type):
        if self.boolean_stack[-1]:
            if v_type != BOOL:
                raise ValueError("Parsing mode cannot be boolean")
            if name not in self.var_to_lit:
                literal = self.new_literal()
                self.var_to_lit[name] = literal
            return self.manager.l(self.var_to_lit[name])
        else:
            if v_type != REAL:
                raise ValueError("Parsing mode cannot be real")
            return PiecewiseXSDD.symbol(name, self.manager, self.algebra)

    def walk_constant(self, value, v_type):
        if self.boolean_stack[-1]:
            if v_type != BOOL:
                raise ValueError("Parsing mode cannot be boolean")
            if value:
                return self.manager.true()
            else:
                return self.manager.false()
        else:
            if v_type != REAL:
                raise ValueError("Parsing mode cannot be real")
            return PiecewiseXSDD.real(value, self.manager, self.algebra)


class PySmtConversion(Semiring):
    def __init__(self, abstractions, var_to_lit):
        super()
        self.reverse_abstractions = {v: k for k, v in abstractions.items()}
        self.lit_to_var = {v: k for k, v in var_to_lit.items()}

    def times_neutral(self):
        return TRUE()

    def plus_neutral(self):
        return FALSE()

    def times(self, a, b, index=None):
        return a & b

    def plus(self, a, b, index=None):
        return a | b

    def negate(self, a):
        return ~a

    def positive_weight(self, a):
        return self.reverse_abstractions[a] if a in self.reverse_abstractions else Symbol(self.lit_to_var[a], BOOL)


def convert_formula(formula, sdd_manager, algebra: Type[AlgebraBackend], abstractions=None, var_to_lit=None)\
        -> SddNode:
    if SddManager is None:
        raise InstallError("The pysdd package is required for this function but is not currently installed.")
    converter = SddConversionWalker(sdd_manager, algebra, True, abstractions, var_to_lit)
    return converter.walk_smt(formula)


def convert_function(formula, sdd_manager, algebra: Type[AlgebraBackend], abstractions=None, var_to_lit=None)\
        -> PiecewiseXSDD:
    if SddManager is None:
        raise InstallError("The pysdd package is required for this function but is not currently installed.")
    converter = SddConversionWalker(sdd_manager, algebra, False, abstractions, var_to_lit)
    return converter.walk_smt(formula)


def recover_formula(sdd_node: SddNode, abstractions, var_to_lit) -> FNode:
    return simplify(amc(PySmtConversion(abstractions, var_to_lit), sdd_node))
