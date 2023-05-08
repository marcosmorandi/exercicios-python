'''
Desafio 030 - Feito
Crie um programa que leia um número inteiro e mostre na tela se ele é Par ou Ímpar.
'''

# Considera-se um número par quando o resto da divisão por 2 é igual a 0.
# Considera-se um número ímpar quando o resto da divisão por 2 é diferente de 0.

numero = int(input('Digite um número inteiro: '))

if (numero % 2) == 0:
    print('Número par!')
else:
    print('Número ímpar!')
