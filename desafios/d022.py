'''
Desafio 022 - Feito
Crie um programa que leia o nome completo de uma pessoa e mostre:
* O nome com todas as letras maiúsculas.
* O nome com todas as letras minúsculas.
* Quantas letras ao todo (sem considerar espaços).
* Quantas letras tem o primeiro nome.
'''

nome_completo = input('Digite o nome completo: ')

print(f'Seu nome em maiúsculas é {nome_completo.upper()}.') # Letras maiúsculas.
print(f'Seu nome em minúsculas é {nome_completo.lower()}.') # Letras minúsculas.

sem_espacos = nome_completo.replace(' ', '') # Quantas letras ao todo (sem considerar espaços).
print(f'Seu nome tem ao todo {len(sem_espacos)} letras.')

divide_nomes = nome_completo.split() # Quantas letras tem o primeiro nome.
print(f'Seu primeiro nome tem {len(divide_nomes[0])} letras.')
