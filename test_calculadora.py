import pytest
from unittest.mock import Mock
from calculadora import Calculadora

def test_suma():
    calc = Calculadora(servicio_externo=None)
    assert calc.suma(2, 3) == 5

def test_resta():
    calc = Calculadora(servicio_externo=None)
    assert calc.resta(5, 2) == 3

def test_multiplicacion():
    calc = Calculadora(servicio_externo=None)
    assert calc.multiplicacion(4, 3) == 12

def test_division():
    calc = Calculadora(servicio_externo=None)
    assert calc.division(10, 2) == 5

def test_division_cero():
    calc = Calculadora(servicio_externo=None)
    with pytest.raises(ValueError):
        calc.division(10, 0)