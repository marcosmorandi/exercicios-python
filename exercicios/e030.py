'''
Exercício 030 - Feito
Crie um programa que leia um número inteiro e mostre na tela se ele é Par ou Ímpar.
'''

numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print(f'O número {numero} é Par!')
else:
    print(f'O número {numero} é Ímpar!')
