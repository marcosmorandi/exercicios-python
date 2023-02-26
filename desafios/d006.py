'''
Desafio 006 - Feito
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''
# Importando o biblioteca "math" para cáculo da raiz quadrada, nesse caso importou toda biblioteca "math".
# Se quiser importar apenas o "sqrt", para poupar memória por exemplo, o comando seria "from math import sqrt".
import math

numero = int(input('Digite um número: '))
numero_dobro = numero * 2
numero_triplo = numero * 3
numero_raiz_quadrada = math.sqrt(numero) # Comando que calcula a raiz quadrada.

print('O número digitado é {}, seu dobro é {}, triplo é {} e raiz quadrada é {}.'.format(numero, numero_dobro, numero_triplo, numero_raiz_quadrada))
