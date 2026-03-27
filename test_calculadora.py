import pytest
from unittest.mock import Mock
from calculadora import Calculadora, suma

def test_suma():
    calc = Calculadora()
    assert calc.suma(2, 3) == 5
