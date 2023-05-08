'''
Desafio 033 - Feito
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))
numero_3 = int(input('Digite o terceiro número: '))

if (numero_1 > numero_2) and (numero_1 > numero_3):
    print(f'O numero {numero_1} é o maior.')
elif (numero_2 > numero_1) and (numero_2 > numero_3):
    print(f'O numero {numero_2} é o maior.')
elif (numero_3 > numero_1) and (numero_3 > numero_2):
    print(f'O numero {numero_3} é o maior.')

if (numero_1 < numero_2) and (numero_1 < numero_3):
    print(f'O numero {numero_1} é o menor.')
elif (numero_2 < numero_1) and (numero_2 < numero_3):
    print(f'O numero {numero_2} é o menor.')
elif (numero_3 < numero_1) and (numero_3 < numero_2):
    print(f'O numero {numero_3} é o menor.')
