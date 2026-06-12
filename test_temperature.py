# Testes de unidades

import pytest

import temperature as t


def test_celsius_para_fahrenheit():
    assert t.celsius_para_fahrenheit(100) == 212
    assert t.celsius_para_fahrenheit(0) == 32
    assert t.celsius_para_fahrenheit(-40) == -40  # ponto onde as escalas se cruzam


def test_fahrenheit_para_celsius():
    assert t.fahrenheit_para_celsius(212) == 100
    assert t.fahrenheit_para_celsius(32) == 0


def test_celsius_para_kelvin():
    assert t.celsius_para_kelvin(0) == 273.15
    assert t.celsius_para_kelvin(-273.15) == 0


def test_kelvin_para_celsius():
    assert t.kelvin_para_celsius(273.15) == 0
    assert t.kelvin_para_celsius(0) == -273.15


def test_fahrenheit_para_kelvin():
    assert t.fahrenheit_para_kelvin(32) == pytest.approx(273.15)


def test_kelvin_para_fahrenheit():
    assert t.kelvin_para_fahrenheit(273.15) == pytest.approx(32)


def test_ida_e_volta():
    """Converter e desconverter deve devolver o valor original."""
    assert t.fahrenheit_para_celsius(t.celsius_para_fahrenheit(37)) == pytest.approx(37)


def test_abaixo_do_zero_absoluto_gera_erro():
    with pytest.raises(ValueError):
        t.celsius_para_kelvin(-300)
    with pytest.raises(ValueError):
        t.kelvin_para_celsius(-1)
