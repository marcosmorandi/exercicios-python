'''
Desafio 036 - Feito
Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o
empréstimo será negado. Desconsidere os juros.
'''

valor_casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual o salário do comprador: '))
anos_pagando = int(input('Em quantos anos vai pagar: '))

prestacao_anual = valor_casa / anos_pagando
prestacao_mensal = prestacao_anual / 12

if prestacao_mensal > (salario * 30 / 100): # Conferindo se a prestação mensal excede 30% do salário.
    print('Emprestimo negado!')
    print('O valor da prestação excede 30% do salário.')
    print(f'Prestação mensal: R$ {prestacao_mensal:.2f}')
else:
    print('Emprestimo aprovado!')
    print(f'Prestação mensal: R$ {prestacao_mensal:.2f}')
