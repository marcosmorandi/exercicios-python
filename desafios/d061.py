'''
Desafio 061 - Feito
Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura "while".
'''

# '''
# Exercício 051 - Feito
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA(progressão aritmética).
# No final, mostre os 10 primeiros termos dessa progressão.
# '''

# primeiro = int(input('Primeiro termo: '))
# razao = int(input('Razão: '))
# decimo = primeiro + (10 -1) * razao # Fórmula do enésimo termo de uma PA.
# for c in range(primeiro, decimo + razao, razao):
#     print(f'{c}', end=' -> ')
# print('Acabou')

print('-=-' * 10)
print('Gerador de PA')
print('-=-' * 10)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 1
print('Os 10 primeiros termos dessa PA são:')
while contador <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    contador += 1
print('FIM')
