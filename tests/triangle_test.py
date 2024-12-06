import sys
import os
import pytest
from triangle import area, perimeter


sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)


def test_area():
    assert area(3, 4, 5) == 6


def test_area_invalid():
    with pytest.raises(TypeError):
        area(3, 5, "9")


def test_invalid_size_area():
    with pytest.raises(TypeError):
        area(3, 5)


def test_perimeter():
    assert perimeter(3, 4, 5) == 12


def test_perimeter_invalid():
    with pytest.raises(TypeError):
        perimeter(3, 4, "5")


def test_invalid_size_perimeter():
    with pytest.raises(TypeError):
        perimeter(3, 5)
