from typing import Dict, Tuple, Union

from pysmt.shortcuts import Plus, Symbol, Real, Times
from pysmt.typing import REAL

from pywmi import SmtWalker
from functools import reduce, partial

CONST_KEY = ()


class Polynomial(object):
    def __init__(self, poly_dict):
        self.poly_dict = poly_dict  # type: Dict[Tuple[str], float]
        self._hash_value = None

    def to_smt(self):
        keys = {key: Times(Symbol(n, REAL) for n in key) if key != CONST_KEY else Real(1.0)
                for key in self.poly_dict.keys()}
        return Plus(
            keys[key] * Real(value) if value != 1 else keys[key]
            for key, value in self.poly_dict.items()
        )

    def __add__(self, other: Union[object, int, float]):
        if isinstance(other, (float, int)):
            other = Polynomial({CONST_KEY: other})

        if not isinstance(other, Polynomial):
            raise NotImplementedError(f"Can only add polynomials not {other}")

        return Polynomial(Polynomial.dict_plus(self.poly_dict, other.poly_dict))

    def __radd__(self, other):
        if isinstance(other, (float, int)):
            return self.__add__(other)
        raise NotImplementedError()

    def __mul__(self, other: Union[object, int, float]):
        if isinstance(other, (float, int)):
            other = Polynomial({CONST_KEY: other})

        if not isinstance(other, Polynomial):
            raise NotImplementedError(f"Can only multiply polynomials not {other}")

        return Polynomial(Polynomial.dict_times(self.poly_dict, other.poly_dict))

    def __rmul__(self, other):
        if isinstance(other, (float, int)):
            return self.__mul__(other)
        raise NotImplementedError()

    @staticmethod
    def dict_plus(dict1, dict2):
        result = dict(dict1)
        for key, value in dict2.items():
            if key in result:
                result[key] += value
            else:
                result[key] = value
        return result

    @staticmethod
    def dict_times(dict1, dict2, force_linear=False):
        result = dict()
        for key1, value1 in dict1.items():
            for key2, value2 in dict2.items():
                if key1 != CONST_KEY and key2 != CONST_KEY and force_linear:
                    raise ValueError(f"Non-linear constraints not supported")
                key = tuple(sorted(key1 + key2))
                result[key] = result.get(key, 0) + value1 * value2
        return result

    @staticmethod
    def from_smt(formula):
        poly_dict = MathDictConverter(force_linear=False).walk_smt(formula)
        poly_dict = {k: v for k, v in poly_dict.items() if v != 0}
        return Polynomial(poly_dict)

    @staticmethod
    def from_constant(constant):
        return Polynomial({CONST_KEY: constant})

    def __hash__(self):
        if not self._hash_value:
            self._hash_value = hash(frozenset(self.poly_dict.items()))
        return self._hash_value

    def __eq__(self, other):
        return isinstance(other, Polynomial) and self.poly_dict == other.poly_dict

    def __str__(self):
        return " + ".join("*".join(str(e) for e in key + (value,)) for key, value in self.poly_dict.items())

    def __repr__(self):
        return self.__str__()


class MathDictConverter(SmtWalker):
    def __init__(self, force_linear=True):
        self.force_linear = force_linear

    def walk_and(self, args):
        raise ValueError(f"AND not supported")

    def walk_or(self, args):
        raise ValueError(f"OR not supported")

    def walk_plus(self, args):
        return reduce(Polynomial.dict_plus, self.walk_smt_multiple(args))

    def walk_minus(self, left, right):
        left_dict, right_dict = self.walk_smt(left), self.walk_smt(right)
        right_dict = {name: -value for name, value in right_dict.items()}
        return Polynomial.dict_plus(left_dict, right_dict)

    def walk_times(self, args):
        return reduce(partial(Polynomial.dict_times, force_linear=self.force_linear), self.walk_smt_multiple(args))

    def walk_not(self, argument):
        raise ValueError(f"NOT not supported")

    def walk_ite(self, if_arg, then_arg, else_arg):
        raise ValueError(f"ITE not supported")

    def walk_pow(self, base, exponent):
        exponent = float(exponent.constant_value())
        if int(exponent) != exponent:
            raise ValueError(f"Fractional powers ({exponent}) are not supported")
        exponent = int(exponent)
        if exponent != 1 and self.force_linear:
            raise ValueError(f"Non-linear constraints are not supported ({base}**{exponent})")
        base = self.walk_smt(base)
        result = base
        for _ in range(exponent - 1):
            result = Polynomial.dict_times(result, base, self.force_linear)
        return result

    def walk_lte(self, left, right):
        result = self.walk_minus(left, right)
        factor = None
        for key in sorted(result.keys()):
            if result[key] != 0:
                factor = abs(result[key])
                break
        if factor is None:
            return {CONST_KEY: 0}
        else:
            return {k: v / factor for k, v in result.items()}

    def walk_lt(self, left, right):
        return self.walk_lte(left, right)

    def walk_equals(self, left, right):
        raise ValueError(f"EQ not supported")

    def walk_symbol(self, name, v_type):
        if v_type == REAL:
            return {(name,): 1}
        else:
            raise ValueError(f"Symbol of type {v_type} not supported")

    def walk_constant(self, value, v_type):
        if v_type == REAL:
            return {CONST_KEY: float(value)}
        else:
            raise ValueError(f"Constant of type {v_type} not supportde")


def get_inequality_dict(formula) -> Dict:
    return MathDictConverter(force_linear=True).walk_smt(formula)


def get_inequality_smt(formula):
    formula_dict = get_inequality_dict(formula)
    return Plus(Times(Symbol(n, REAL) for n in name) * Real(factor)
                if factor != 1 else Times(Symbol(n, REAL) for n in name)
                for name, factor in formula_dict.items() if name != CONST_KEY) \
           <= Real(-formula_dict.get(CONST_KEY, 0))
