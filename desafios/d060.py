'''
Desafio 060 - Feito
Faça um programa que leia um número qualquer e mostre o seu fatorial.
EX: 5!=5x4x3x2x1=120
'''

numero = int(input('Digite um número para calcular seu fatorial: '))
contador = numero
fatorial = 1 # Fator nulo de multiplicação é 1. Nulo de soma ou subtração é 0.
print(f'Calculando {numero} ! = ', end='') # "end=''" para não pular linha.
while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='') # É possível usar "if", "else" dentro de um "print".
    fatorial *= contador
    contador -= 1
print(f'{fatorial}')
