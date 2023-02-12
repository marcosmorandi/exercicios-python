'''
Desafio 010 - Feito
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
Considere US$ 1,00 = R$ 5,22 ou a cotação atual.
'''

reais = float(input('Quanto dinheiro em R$ tem disponínel: '))

# Conversão de Reais para Dólar.
# 1 / 5,2151
# Cotação do Dólar em 12/02/2023 10h52.

dolar = reais / 5.2151

print('Você pode comprar US$: {:.2f}'.format(dolar))
