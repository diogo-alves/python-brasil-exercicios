from utils import input_number, input_option


def measure_IBW(height, gender):
    """
    Calcula o peso ideal de uma pessoa com base na sua altura e gênero
    """
    formulas = {
        'M': 72.7 * height - 58,
        'F': 62.1 * height - 44.7
    }
    return formulas.get(gender.upper())


def main():
    """
    13. Tendo como dado de entrada a altura (h) de uma pessoa, construa
    um algoritmo que calcule seu peso ideal, utilizando as seguintes 
    fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
    """
    height = input_number('Informe a altura (m): ', numeric_type=float)
    gender = input_option(
        'Informe o gênero (M - Masculino, F - Feminino): ',
        valid_options='mMfF'
    )
    ideal_weight = measure_IBW(height, gender)
    print(f'Seu peso ideal é {ideal_weight:.1f}')


if __name__ == '__main__':
    main()
