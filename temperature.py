"""Conversor de temperatura entre Celsius, Fahrenheit e Kelvin."""

ZERO_ABSOLUTO_C = -273.15
ZERO_ABSOLUTO_F = -459.67
ZERO_ABSOLUTO_K = 0.0


def celsius_para_fahrenheit(celsius):
    if celsius < ZERO_ABSOLUTO_C:
        raise ValueError("Temperatura abaixo do zero absoluto.")
    return celsius * 9 / 5 + 32


def fahrenheit_para_celsius(fahrenheit):
    if fahrenheit < ZERO_ABSOLUTO_F:
        raise ValueError("Temperatura abaixo do zero absoluto.")
    return (fahrenheit - 32) * 5 / 9


def celsius_para_kelvin(celsius):
    if celsius < ZERO_ABSOLUTO_C:
        raise ValueError("Temperatura abaixo do zero absoluto.")
    return celsius + 273.15


def kelvin_para_celsius(kelvin):
    if kelvin < ZERO_ABSOLUTO_K:
        raise ValueError("Temperatura abaixo do zero absoluto.")
    return kelvin - 273.15


def fahrenheit_para_kelvin(fahrenheit):
    return celsius_para_kelvin(fahrenheit_para_celsius(fahrenheit))


def kelvin_para_fahrenheit(kelvin):
    return celsius_para_fahrenheit(kelvin_para_celsius(kelvin))


def main():
    print("Conversor de Temperatura")
    print(f"100 °C = {celsius_para_fahrenheit(100)} °F")
    print(f"32 °F  = {fahrenheit_para_celsius(32)} °C")
    print(f"0 °C   = {celsius_para_kelvin(0)} K")


if __name__ == "__main__":
    main()
