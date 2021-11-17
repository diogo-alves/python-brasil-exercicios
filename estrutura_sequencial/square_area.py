from utils import input_number


def square_area(side_size):
    """Calcula a área do quadrado"""
    return side_size ** 2


def main():
    """
    7. Faça um programa que calcule a área de um quadrado, em seguida 
    mostre o dobro desta área para o usuário.
    """
    side_size = input_number("Informe a medida dos lados: ")
    area = square_area(side_size)
    print(f'O dobro da área do quadrado é {area * 2}.')


if __name__ == '__main__':
    main()
