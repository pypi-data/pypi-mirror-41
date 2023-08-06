import pytest
from pysmt.shortcuts import Ite, Real

from pywmi import Domain, RejectionEngine, XaddEngine
from pywmi.engines.xsdd.inference import NativeXsddEngine
from pywmi.engines.xadd import XaddIntegrator

try:
    import pysdd
    pysdd_installed = True
except ImportError:
    pysdd_installed = False

pytestmark = pytest.mark.skipif(not pysdd_installed, reason="pysdd is not installed")

ERROR = 0.1


def test_volume():
    # Support:  (a | b) & (~a | ~b) & (x >= 0) & (x <= y) & (y <= 10)
    # Weight:   {
    #                a  b  (x>=0.5): 0.6*0.8*(0.5x+0.1y)  0.5 <= x <= y, x <= y <= 10
    #                a  b !(x>=0.5): 0.6*0.8*(0.1x+0.7y)  0 <= x <= [y, 0.5], x <= y <= 10
    #                a !b  (x>=0.5): 0.6*0.2*(0.5x+0.1y)  0.5 <= x <= y, x <= y <= 10
    #                a !b !(x>=0.5): 0.6*0.2*(0.1x+0.7y)  0 <= x <= [y, 0.5], x <= y <= 10
    #               !a  b  (x>=0.5): 0.4*0.8*(0.5x+0.1y)  0.5 <= x <= y, x <= y <= 10
    #               !a  b !(x>=0.5): 0.4*0.8*(0.1x+0.7y)  0 <= x <= [y, 0.5], x <= y <= 10
    #               !a !b  (x>=0.5): 0.4*0.2*(0.5x+0.1y)  0.5 <= x <= y, x <= y <= 10
    #               !a !b !(x>=0.5): 0.4*0.2*(0.1x+0.7y)  0 <= x <= [y, 0.5], x <= y <= 10
    # }

    # TODO What if we don't expand the Weight Function, only compile the support?
    # TODO => Can we reuse the SDD? It doesn't seem so... => Need multiple SDDs to use caching

    domain = Domain.make(["a", "b"], ["x", "y"], [(0, 1), (0, 1)])
    a, b, x, y = domain.get_symbols(domain.variables)
    support = (a | b) & (~a | ~b) & (x >= 0.0) & (x <= y) & (y <= 1.0)
    weight = Ite(a, Real(0.6), Real(0.4)) * Ite(b, Real(0.8), Real(0.2))\
             * (Ite(x >= Real(0.5), Real(0.5) * x + Real(0.1) * y, Real(0.1) * x + Real(0.7) * y))
    xsdd = NativeXsddEngine(domain, support, weight, XaddIntegrator())
    computed_volume = xsdd.compute_volume()
    correction_volume_rej = RejectionEngine(domain, support, weight, 1000000).compute_volume()
    correction_volume_xadd = XaddEngine(domain, support, weight).compute_volume()
    print(correction_volume_rej, correction_volume_xadd, computed_volume)
    assert computed_volume == pytest.approx(correction_volume_rej, rel=ERROR)
    assert computed_volume == pytest.approx(correction_volume_xadd, rel=ERROR)


def test_trivial_weight_function():
    # Support:  (a | b) & (~a | ~b) & (x >= 0) & (x <= y) & (y <= 10)
    # Weight:   1

    domain = Domain.make(["a", "b"], ["x", "y"], [(0, 1), (0, 1)])
    a, b, x, y = domain.get_symbols(domain.variables)
    support = (a | b) & (~a | ~b) & (x >= 0) & (x <= y) & (y <= 1)
    weight = Real(1.0)
    xsdd = NativeXsddEngine(domain, support, weight, XaddIntegrator())
    computed_volume = xsdd.compute_volume()
    correction_volume_rej = RejectionEngine(domain, support, weight, 1000000).compute_volume()
    correction_volume_xadd = XaddEngine(domain, support, weight).compute_volume()
    print(correction_volume_rej, correction_volume_xadd, computed_volume)
    assert computed_volume == pytest.approx(correction_volume_rej, rel=ERROR)
    assert computed_volume == pytest.approx(correction_volume_xadd, rel=ERROR)
