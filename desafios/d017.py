'''
Desafio 017 - Feito
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo...
retângulo, calcule e mostre o comprimento da hipotenusa.
'''

import math

# leitura dos comprimentos dos catetos
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

# cálculo da hipotenusa
hipotenusa = math.sqrt(cateto_oposto ** 2  + cateto_adjacente ** 2)

# exibição do resultado
print(f'A hipotenusa do triângulo retângulo é {hipotenusa:.2f}')
