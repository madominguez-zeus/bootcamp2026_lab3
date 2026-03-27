import pytest
from unittest.mock import MagicMock
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

def test_obtener_valor_api_externo():
    servicio_mock = MagicMock()
    
    #Simulación de llamada al servicio externo con valor 42
    servicio_mock.obtener_valor.return_value = 42
    calc = Calculadora(servicio_externo=servicio_mock)

    #Llamada al método que utiliza el servicio externo
    valor = calc.servicio_externo.obtener_valor()
    assert valor == 42
    servicio_mock.obtener_valor.assert_called_once()