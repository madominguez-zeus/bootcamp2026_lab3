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

def test_obtener_valor_multiples_set():
    servicio_mock = MagicMock()
    test_valores = [10, 20, 30]

    #side_effect permite simular múltiples llamadas al método obtener_valor con diferentes resultados
    servicio_mock.obtener_valor.side_effect = test_valores

    calc = Calculadora(servicio_externo=servicio_mock)

    assert calc.servicio_externo.obtener_valor() == test_valores[0]
    assert calc.servicio_externo.obtener_valor() == test_valores[1]
    assert calc.servicio_externo.obtener_valor() == test_valores[2]
    assert servicio_mock.obtener_valor.call_count == 3

def test_obtener_valor_cuenta():
    servicio_mock = MagicMock()
    cantidad_de_llamadas = 10

    calc = Calculadora(servicio_externo=servicio_mock)

    for _ in range(cantidad_de_llamadas):
        calc.servicio_externo.obtener_valor()

    assert calc.servicio_externo.obtener_valor.call_count == cantidad_de_llamadas

def test_servicio_complejo():
    servicio_mock = MagicMock()
    servicio_mock.obtener_valor.return_value = 50
    servicio_mock.otro_metodo.return_value = "resultado"
    servicio_mock.atributo = "valor_atributo"

    calc = Calculadora(servicio_externo=servicio_mock)
    assert calc.servicio_externo.obtener_valor() == 50
    assert calc.servicio_externo.otro_metodo() == "resultado"
    assert calc.servicio_externo.atributo == "valor_atributo"

def test_servicio_contextual():
    servicio_mock = MagicMock()
    servicio_mock.__enter__.return_value = "Dentro del Contexto"
    servicio_mock.__exit__.return_value = None

    with servicio_mock as resultado:
        assert resultado == "Dentro del Contexto"

    servicio_mock.__enter__.assert_called_once()
    servicio_mock.__exit__.assert_called_once()