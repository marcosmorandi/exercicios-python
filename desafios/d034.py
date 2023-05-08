'''
Desafio 034 - Feito
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00 calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''

salario = float(input('Qual o salário do funcionário: '))

if (salario > 1250.00):
    aumento = salario + (salario * 0.10)
    print(f'Salario anterior de R$ {salario:.2f}, com o aumento de 10% fica {aumento:.2f}.')
else:
    aumento = salario + (salario * 0.15)
    print(f'Salario anterior de R$ {salario:.2f}, com o aumento de 15% fica {aumento:.2f}.')
