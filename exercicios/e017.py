'''
Exercício 017
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo...
retângulo, calcule e mostre o comprimento da hipotenusa.
'''

# 1ª forma.
co = float(input('(1ª)Comprimento do cateto oposto: '))
ca = float(input('(1ª)Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('(1ª)A hipotenusa vai medir {:.2f}'.format(hi))

# 2ª forma.
import math # O "import" não funciona apenas no começo do código, pode ser usado ao longo dele.
co = float(input('(2ª)Comprimento do cateto oposto: '))
ca = float(input('(2ª)Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca) # "hypot" é o cáculo da hipotenusa da biblioteca "math".
print('(2ª)A hipotenusa vai medir {:.2f}'.format(hi))

# 3ª forma.
from math import hypot # O "from" "import" não funciona apenas no começo do código, pode ser usado ao longo dele.
co = float(input('(3ª)Comprimento do cateto oposto: '))
ca = float(input('(3ª)Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('(3ª)A hipotenusa vai medir {:.2f}'.format(hi))
