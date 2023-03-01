'''
Desafio 016 - Feito
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.
Ex:
Digite um numero: 6.127
O número 6.127 tem a parte inteira 6.
'''

# Importando apenas o "trunc" da biblioteca "math".
from math import trunc

numero = float(input('Digite um número real (com "."): '))
inteiro = trunc(numero)

print('Do número digitado {}, a parte inteira é {}.'.format(numero, inteiro))
