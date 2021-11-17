from utils import input_number


def average_grade(grades):
    """Retorna a média das notas informadas"""
    return sum(grades)/len(grades)


def main():
    """
    4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
    """
    grades = [
        input_number(f'Informe a {nth}ª nota: ', numeric_type=float)
        for nth in range(1, 5)
    ]
    average = average_grade(grades)
    print(f'A média das notas é {average:.1f}.')


if __name__ == '__main__':
    main()
