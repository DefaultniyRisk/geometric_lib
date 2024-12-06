import sys
import os
import math
import pytest
from calculate import calc
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)


def test_square_area():
    result = calc('square', 'area', [3])
    expected_result = 9
    assert result == expected_result


def test_square_perimeter():
    result = calc('square', 'perimeter', [3])
    expected_result = 12
    assert result == expected_result


def test_circle_area():
    result = calc('circle', 'area', [4])
    expected_result = math.pi * 4 * 4
    assert result == pytest.approx(expected_result, rel=1e-2)


def test_circle_perimeter():
    result = calc('circle', 'perimeter', [4])
    expected_result = 2 * math.pi * 4
    assert result == pytest.approx(expected_result, rel=1e-2)


def test_triangle_area():
    result = calc('triangle', 'area', [3, 4, 5])
    assert result == 6


def test_invalid_size_square():
    with pytest.raises(AssertionError, match="Error"):
        calc('circle', 'area', [3, 5, 9])


def test_invalid_size_circle():
    with pytest.raises(AssertionError, match="Error"):
        calc('circle', 'area', [1, 4, 2])


def test_triangle_perimeter():
    result = calc('triangle', 'perimeter', [3, 4, 5])
    assert result == 12


def test_invalid_function():
    with pytest.raises(AssertionError, match="Error"):
        calc('circle', 'speed', [3])


def test_invalid_figure():
    with pytest.raises(AssertionError, match="Error"):
        calc('oval', 'area', [1])


def test_invalid_size_triangle():
    with pytest.raises(AssertionError, match="Error"):
        calc('triangle', 'area', [7])
