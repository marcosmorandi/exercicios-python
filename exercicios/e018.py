'''
Exercício 018 - Feito
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno...
e tangente desse ângulo.
'''

# 1ª forma.
import math
angulo = float(input('(1ª)Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('(1ª)O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('(1ª)O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('(1ª)O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))

# 2ª forma.
from math import radians, sin, cos, tan
angulo = float(input('(2ª)Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print('(2ª)O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('(2ª)O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('(2ª)O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
