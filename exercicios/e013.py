'''
Exercício 013 - Feito
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''

salario = float(input('Qual é o salário do funcinário? R$ '))
novo_salario = salario + (salario * 15 / 100) # "15 / 100" nessa cálculo significa 15%.
print('Um funcionário que ganhava R$ {:.2f}, com 15% de aumento, passa a receber R$ {:.2f}'.format(salario, novo_salario))
