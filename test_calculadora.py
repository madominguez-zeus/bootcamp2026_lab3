import pytest
from unittest.mock import Mock
from calculadora import Calculadora, suma, resta, multiplicacion

def test_suma():
    calc = Calculadora()
    assert calc.suma(2, 3) == 5

def test_resta():
    calc = Calculadora()
    assert calc.resta(5, 2) == 3

