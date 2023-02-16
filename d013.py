'''
Desafio 013 - Feito
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''

salario  = float(input('Qual o salário atual do funcionário em R$: '))

novo_salario = salario + (salario * 0.15)

print('O salário que antes era de R$ {:.2f}, agora com 15% de aumento é de R$ {:.2f}.'.format(salario, novo_salario))
