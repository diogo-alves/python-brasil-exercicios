from utils import input_number


def to_celsius(fahrenheit):
    """Converte temperatura em graus Fahrenheit para Celsius"""
    return (fahrenheit - 32) / 1.8


def main():
    """
    9. Faça um programa que peça a temperatura em graus Fahrenheit, 
    transforme e mostre a temperatura em graus Celsius. 
    """
    fahrenheit = input_number(
        'Insira a temperatura em graus Fahrenheit: ', numeric_type=float
    )
    celsius = to_celsius(fahrenheit)
    print(f'A temperatura convertida em graus Celsius é {celsius}.')


if __name__ == '__main__':
    main()
