from utils import input_number


def main():
    """3. Faça um Programa que peça dois números e imprima a soma."""
    number1 = input_number('Informe o 1º número a ser somado: ')
    number2 = input_number('Informe o 2º número a ser somado: ')
    total = number1 + number2
    print(f'A soma de {number1} + {number2} = {total}')


if __name__ == '__main__':
    main()
