'''
Exercício 060 - Feito
Faça um programa que leia um número qualquer e mostre o seu fatorial.
EX: 5!=5x4x3x2x1=120
'''

# Primeira forma, importanto biblioteca:
# from math import factorial
# n = int(input('Digite um número para calcular seu Fatorial: '))
# f = factorial(n)
# print(f'O fatorial de {n} é {f}.')

# Segunda forma, manual:
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1 # Fator nulo de multiplicação é 1. Nulo de soma ou subtração é 0.
print(f'Calculando {n} ! = ', end='') # "end=''" para não pular linha.
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='') # É possível usar um "if" "else" dentro de um "print".
    f *= c
    c -= 1
print(f'{f}')
