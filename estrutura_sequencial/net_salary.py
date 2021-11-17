from salary import monthly_salary
from utils import input_number

SOCIAL_SECURITY_RATE = 0.08
INCOME_TAX_RATE = 0.11
UNION_RATE = 0.05


def calculate_social_security_tax(calculation_basis):
    """Calcula o valor da contribuição do INSS"""
    return calculation_basis * SOCIAL_SECURITY_RATE


def calculate_income_tax(calculation_basis):
    """Calcula o valor do imposto de renda retino na fonte"""
    return calculation_basis * INCOME_TAX_RATE


def calculate_union_dues(calculation_basis):
    """Calcula o valor da contribuição sindical"""
    return calculation_basis * UNION_RATE


def main():
    """
    15. Faça um Programa que pergunte quanto você ganha por hora e o
    número de horas trabalhadas no mês. Calcule e mostre o total do seu
    salário no referido mês, sabendo-se que são descontados 11% para o
    Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um
    programa que nos dê:
    a) salário bruto.
    b) quanto pagou ao INSS.
    c) quanto pagou ao sindicato.
    d) o salário líquido.
    e) calcule os descontos e o salário líquido, conforme a tabela
       abaixo:
       + Salário Bruto : R$
       - IR (11%) : R$
       - INSS (8%) : R$
       - Sindicato ( 5%) : R$
       = Salário Liquido : R$
       Obs.: Salário Bruto - Descontos = Salário Líquido.
    """
    wage = input_number(
        'Informe o valor ganho por hora: ', numeric_type=float
    )
    working_hours = input_number(
        'Informe o número de horas/mês trabalhadas: ', numeric_type=float
    )
    gross_salary = monthly_salary(wage, working_hours)
    social_security = calculate_social_security_tax(gross_salary)
    income_tax = calculate_income_tax(gross_salary - social_security)
    union_dues = calculate_union_dues(gross_salary)
    net_salary = gross_salary - social_security - income_tax - union_dues
    print(f'+ Salário Bruto :   R$ {gross_salary:.2f}')
    print(f'- IR (11%) :        R$ {income_tax:.2f}')
    print(f'- INSS (8%) :       R$ {social_security:.2f}')
    print(f'- Sindicato (5%)  : R$ {union_dues:.2f}')
    print(f'= Salário Liquido : R$ {net_salary:.2f}')


if __name__ == '__main__':
    main()
