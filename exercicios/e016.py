'''
Exercício 016 - Feito
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.
Ex:
Digite um numero: 6.127
O número 6.127 tem a parte inteira 6.
'''

# 1ª forma, importando toda a biblioteca "math".
import math
num = float(input('(1ª)Digite um valor: '))
print('O valor digitado foi {} e sua porção interia é {}.'.format(num, math.trunc(num)))

# 2ª forma, importando somente a função "trunch" da biblioteca "math".
from math import trunc
num = float(input('(2ª)Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}.'.format(num, trunc(num)))

# 3ª forma. Nem sempre é necessário importar módulos.
num = float(input('(3ª)Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, int(num)))

# 4ª forma. Também não é necessário importar módulos.
num = float(input('(4ª)Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {:.0f}.'.format(num, num))
