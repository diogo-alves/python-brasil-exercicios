import math

from utils import input_number, pluralize

CAN_PRICE = 80.00
LITERS_PER_CAN = 18
LITERS_PER_SQUARE_METER = 1 / 3


def estimate_cans(paint_area):
    """
    Estima a quantidade necessária de latas de tinta para a pintar a
    área informada
    """
    liters = _calculate_liters(paint_area)
    return math.ceil(liters / LITERS_PER_CAN)


def _calculate_liters(paint_area):
    """
    Calcula a quantidade necessária de litros de tinta para pintar a
    área informada
    """
    return paint_area * LITERS_PER_SQUARE_METER


def total_cost(cans):
    """
    Calcula o custo total da quantidade informada de latas de tinta
    """
    return cans * CAN_PRICE


def main():
    """
    16. Faça um programa para uma loja de tintas. O programa deverá
    pedir o tamanho em metros quadrados da área a ser pintada. Considere
    que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e
    que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
    Informe ao usuário a quantidades de latas de tinta a serem compradas
    e o preço total.
    """
    paint_area = input_number(
        'Informe a medida da área a ser pintada (m²): ',
        numeric_type=float
    )
    cans = estimate_cans(paint_area)
    total = total_cost(cans)
    print(
        f'Será necessário comprar {cans} {pluralize(cans, "lata")} de tinta '
        f'ao custo de R${total:.2f}.'
    )


if __name__ == '__main__':
    main()
