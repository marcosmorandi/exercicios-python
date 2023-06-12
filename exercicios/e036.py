'''
Exercício 036
Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o
empréstimo será negado. Desconsidere os juros.
'''

casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))

prestacao = casa / (anos * 12)
minimo = salario * 30 / 100 # 30% do salário.

print(f'Para pagar uma casa de R$ {casa:.2f} em {anos} anos a prestação será de {prestacao:.2f}')

if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
