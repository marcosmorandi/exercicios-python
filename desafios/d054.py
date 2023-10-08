'''
Desafio 054 - Feito
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores.
'''

from datetime import date
maior_idade = 0
menor_idade = 0
for c in range(1, 8):
    ano_nascimento = int(input('Digite o ano de nascimento: '))
    if date.today().year - ano_nascimento >= 18:
        maior_idade = maior_idade + 1
    else:
        menor_idade = menor_idade + 1
print(f'{maior_idade} pessoas são maiores de idade e {menor_idade} são menores de idade.')
