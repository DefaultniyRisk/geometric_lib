import sys
import os
import pytest
from square import area, perimeter
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)


def test_area():
    result = area(3)
    assert result == 9


def test_area_invalid():
    with pytest.raises(TypeError):
        area("9")


def test_perimeter():
    result = perimeter(3)
    assert result == 12


def test_invalid_size_perimeter():
    with pytest.raises(TypeError):
        perimeter(6, 24)
