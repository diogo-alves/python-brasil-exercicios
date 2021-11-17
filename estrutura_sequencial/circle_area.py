import math

from utils import input_number


def circle_area(radius_size):
    """Calcula a área do círculo"""
    return math.pi * radius_size ** 2


def main():
    """
    6. Faça um Programa que peça o raio de um círculo, 
    calcule e mostre sua área.
    """
    radius_size = input_number('Informe a medida do raio: ')
    area = circle_area(radius_size)
    print(f'A área do círculo é {area:.2f}')


if __name__ == '__main__':
    main()
