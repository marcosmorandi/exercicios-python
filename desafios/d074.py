'''
Desafio 074 - Feito
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

from random import randint
numeros = (randint(0, 9), randint(0, 9), randint (0, 9), randint (0, 9), randint (0, 9))
print(f'Numeros gerados: {numeros}')
print(f'Números em ordem crescente: {(sorted(numeros))}')
print(f'Menor número: {min(numeros)}') # "min(numeros)" mostra o menor número gerado.
print(f'Maior número: {max(numeros)}') # "max(numeros)" mostra o maior número gerado.

# Laço de repetição para visualizar sem os parenteses.
# print('Os valores sorteados foram: ', end='')
# for n in numeros:
#     print(f'{n} ', end='')
# print(f'\nO maior valor sorteado foi: {max(numeros)}')
# print(f'O menor valor sorteado foi: {min(numeros)}')
