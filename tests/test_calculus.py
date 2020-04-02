import math
import pytest

from calculus import __version__, integral


def test_version():
    assert __version__ == '0.1.0'


def test_simple_integral_approximation():
    assert integral(
        lambda x: math.log(math.e) * x, (0, 1), 10000000
        ) == pytest.approx(.5)

    assert integral(
        lambda x: math.exp(x) / x, (1, 3), 10000000
    ) == pytest.approx(8.03871475426948)
