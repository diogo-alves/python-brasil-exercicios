from utils import input_number


def measure_IBW(height):
    """Calcula o peso ideal de uma pessoa com base na sua altura"""
    return 72.7 * height - 58


def main():
    """
    12. Tendo como dados de entrada a altura de uma pessoa, construa um 
    algoritmo que calcule seu peso ideal, usando a seguinte fórmula: 
    (72.7*altura) - 58
    """
    height = input_number('Informe a altura (m): ', numeric_type=float)
    ideal_weight = measure_IBW(height)
    print(f'Seu peso ideal é {ideal_weight:.1f}')


if __name__ == '__main__':
    main()
