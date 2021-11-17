from utils import input_number


def main():
    """
    11. Faça um Programa que peça 2 números inteiros e um número real. 
    Calcule e mostre:
    o produto do dobro do primeiro com metade do segundo.
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo.
    """
    number1 = input_number('Informe o 1º número: ')
    number2 = input_number('Informe o 2º número: ')
    number3 = input_number('Informe o 3º número: ', numeric_type=float)
    a = number1 * 2 * number2 / 2
    b = number1 * 3 + number3
    c = number3 ** 3
    print(f'O produto do dobro do 1º número com metade do 2º é {a}')
    print(f'A soma do triplo do 1º número com o 3º é {b}')
    print(f'o 3º número elevado ao cubo é {c}')


if __name__ == '__main__':
    main()
