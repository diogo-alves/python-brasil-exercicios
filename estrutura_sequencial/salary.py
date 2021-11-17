from utils import input_number


def monthly_salary(hourly_wage, monthly_working_hours):
    """
    Calcula o salário a partir do valor da hora trabalhada e do número
    mensal de horas trabalhadas
    """
    return hourly_wage * monthly_working_hours


def main():
    """
    8. Faça um programa que pergunte quanto você ganha por hora e o
    número de horas trabalhadas no mês. Calcule e mostre o total do seu 
    salário no referido mês.
    """
    wage = input_number(
        'Informe o valor ganho por hora: ', numeric_type=float
    )
    working_hours = input_number(
        'Informe o número de horas/mês trabalhadas: ', numeric_type=float
    )
    salary = monthly_salary(wage, working_hours)
    print(f'O total do salário recebido no mês é {salary:.2f}')


if __name__ == '__main__':
    main()
