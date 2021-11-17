from utils import input_number


def to_fahrenheit(celsius):
    """Converte temperatura em graus Celsius para Fahrenheit"""
    return celsius * 1.8 + 32


def main():
    """
    10. Faça um programa que peça a temperatura em graus Celsius, 
    transforme e mostre a temperatura em graus Fahrenheit. 
    """
    celsius = input_number(
        'Insira a temperatura em graus Celsius: ', numeric_type=float
    )
    fahrenheit = to_fahrenheit(celsius)
    print(f'A temperatura convertida em graus Fahrenheit é {fahrenheit}.')


if __name__ == '__main__':
    main()
