from utils import input_number


def main():
    """
    2. Faça um Programa que peça um número e então mostre a mensagem 
    "O número informado foi [número]".
    """
    number = input_number('Insira um número: ')
    print(f'O número informado foi {number}.')


if __name__ == '__main__':
    main()
