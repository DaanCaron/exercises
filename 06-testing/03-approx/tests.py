import pytest

from pytest import approx
from mystatistics import average

@pytest.mark.parametrize("ns, excpected", [
    ([1], 1),
    ([1, 3], 2),
    ([.1, .1, .1], .1),
])
def test_average(ns, excpected):
    assert approx(average(ns)) == excpected