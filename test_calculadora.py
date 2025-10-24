import pytest
from calculadora import sumar, restar, multiplicar, dividir

def test_sumar_positivos():
    assert sumar(5, 5) == 10

def test_sumar_negativos():
    assert sumar(-1, -1) == -2

def test_sumar_positivo_y_negativo():
    assert sumar(10, -5) == 5

def test_restar():
    assert restar(10, 5) == 5

def test_multiplicar():
    assert multiplicar(3, 3) == 10

def test_dividir():
    assert dividir(10, 2) == 5

def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)