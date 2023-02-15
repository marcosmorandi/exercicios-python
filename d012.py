'''
Desafio 012 - Feito
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''

preco = float(input('Qual o preço do produto em R$: '))

novo_preco = preco - (preco * 0.05)

print('O preço que antes era R$ {:.2f}, agora com 5% de desconto é R$ {:.2f}.'.format(preco, novo_preco))
