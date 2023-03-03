'''
Exercício 012 - Feito
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''

# Forma simples de cálcular porcentagem:
# 10*5/100 == 0.5 (5% de R$ 10,00)
# 1500*10/100 == 150.00 (10% de R$ 1.500,00)
# 875*15/100 == 131.25 (15% de R$ 875,00)

preco = float(input('Qual é o preço do produto? R$ '))
novo_preco = preco - (preco * 5 / 100)
print('O produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar R$ {:.2f}'.format(preco, novo_preco))
