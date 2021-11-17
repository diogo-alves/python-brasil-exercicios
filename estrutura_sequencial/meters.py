from utils import input_number


def to_centimeters(meters):
    """Converte metros em centímetros"""
    return meters * 100


def main():
    """5. Faça um programa que converta metros para centímetros."""
    meters = input_number('Informe o valor em metros: ')
    centimeters = to_centimeters(meters)
    print(f'O valor {meters} em metros equivale a {centimeters} centímetros.')


if __name__ == '__main__':
    main()
