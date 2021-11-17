from utils import input_number

LIMIT_WEIGHT_PER_DAY = 50
PENALTY_RATE_PER_KG = 4.00


def get_overfishing(weight):
    """Calcula o peso excedido de peixes pescados no dia"""
    if weight <= LIMIT_WEIGHT_PER_DAY:
        return 0
    return weight - LIMIT_WEIGHT_PER_DAY


def generate_penalty(overweight):
    """Calcula a multa por pesca predatória com base no peso excedido"""
    return overweight * PENALTY_RATE_PER_KG


def main():
    """
    15. João Papo-de-Pescador, homem de bem, comprou um microcomputador
    para controlar o rendimento diário de seu trabalho. Toda vez que ele
    traz um peso de peixes maior que o estabelecido pelo regulamento de
    pesca do estado de São Paulo (50 quilos) deve pagar uma multa de 
    R$ 4,00 por quilo excedente. João precisa que você faça um programa
    que leia a variável peso (peso de peixes) e calcule o excesso.
    Gravar na variável excesso a quantidade de quilos além do limite e
    na variável multa o valor da multa que João deverá pagar. Imprima os
    dados do programa com as mensagens adequadas.
    """
    weight = input_number(
        'Informe a quantidade de peixes pescados (kg): ',
        numeric_type=float
    )
    overfishing = get_overfishing(weight)
    if overfishing:
        print(f'O excedente de peixes pescados foi {overfishing:.2f} kg')
        fine = generate_penalty(overfishing)
        print(f'o valor da multa que João deverá pagar é R${fine:.2f}')
    else:
        print('A quantidade pescada está dentro dos limites legais.')


if __name__ == '__main__':
    main()
