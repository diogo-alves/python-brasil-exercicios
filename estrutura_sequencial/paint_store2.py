import math

from utils import input_number, pluralize

CAN_PRICE = 80.00
EXTRA_LITERS_RATE = 1.1
GALLON_PRICE = 25.00
LITERS_PER_CAN = 18
LITERS_PER_GALLON = 3.6
LITERS_PER_SQUARE_METER = 1 / 6


def estimate_cans(paint_area):
    """
    Estima a quantidade de latas de tinta necessária para a pintar a
    área informada
    """
    liters = calculate_liters(paint_area)
    return math.ceil(liters / LITERS_PER_CAN)


def estimate_gallons(paint_area):
    """
    Estima a quantidade de galões de tinta necessária para a pintar a
    área informada
    """
    liters = calculate_liters(paint_area)
    return math.ceil(liters / LITERS_PER_GALLON)


def calculate_liters(paint_area):
    """
    Calcula a quantidade de litros de tinta necessária para pintar a
    área informada
    """
    if paint_area <= 0:
        return 0
    liters = paint_area * LITERS_PER_SQUARE_METER
    liters *= EXTRA_LITERS_RATE
    return liters


def cans_cost(quantity):
    """
    Calcula o custo total da quantidade informada de latas de tinta
    """
    return _items_value(quantity, CAN_PRICE)


def gallons_cost(quantity):
    """
    Calcula o custo total da quantidade informada de galões de tinta
    """
    return _items_value(quantity, GALLON_PRICE)


def _items_value(quantity, unit_price):
    """Calcula o custo total dos items"""
    return quantity * unit_price


def optimize_cost(paint_area):
    """Estima o menor custo para pintar a área informada"""
    liters = calculate_liters(paint_area)
    cans = int(liters / LITERS_PER_CAN)
    remaining_liters = liters % LITERS_PER_CAN
    gallons = math.ceil(remaining_liters / LITERS_PER_GALLON)
    return cans, gallons


def main():
    """
    17. Faça um Programa para uma loja de tintas. O programa deverá
    pedir o tamanho em metros quadrados da área a ser pintada. Considere
    que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
    que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou
    em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os
    respectivos preços em 3 situações:
    * comprar apenas latas de 18 litros;
    * comprar apenas galões de 3,6 litros;
    * misturar latas e galões, de forma que o desperdício de tinta seja
    menor.
    Acrescente 10% de folga e sempre arredonde os valores para
    cima, isto é, considere latas cheias.
    """
    paint_area = input_number(
        'Informe a área a ser pintada (m²): ',
        numeric_type=float
    )
    template_message = (
        'Será necessário comprar {quantity} {item} de tinta '
        'ao custo de R${cost:.2f}.'
    )
    liters = calculate_liters(paint_area)
    print(f'Tinta necessária: {liters:.1f} {pluralize(liters, "litro")}')

    print('SIMULAÇÃO 1')
    cans = estimate_cans(paint_area)
    print(template_message.format(
        quantity=cans,
        item=pluralize(cans, 'lata'),
        cost=cans_cost(cans)
    ))

    print('SIMULAÇÃO 2')
    gallons = estimate_gallons(paint_area)
    print(template_message.format(
        quantity=gallons,
        item=pluralize(gallons, 'galão', 'galões'),
        cost=gallons_cost(gallons)
    ))

    print('SIMULAÇÃO 3')
    cans, gallons = optimize_cost(paint_area)
    print(template_message.format(
        quantity=cans,
        item=pluralize(cans, 'lata'),
        cost=cans_cost(cans)
    ))
    print(template_message.format(
        quantity=gallons,
        item=pluralize(gallons, 'galão', 'galões'),
        cost=gallons_cost(gallons)
    ))


if __name__ == '__main__':
    main()
