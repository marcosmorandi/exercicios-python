'''
Exercício 010 - Feito
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
Considere US$ 1,00 = R$ 5,22 ou a cotação atual.
'''

real = float(input('Quanto de dinheiro você tem na carteira? R$ '))
dolar = real / 5.22

print('Com R$ {:.2f} você pode comprar US$ {:.2f}'.format(real, dolar))
