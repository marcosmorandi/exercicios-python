'''
Desafio 022 - Feito
Crie um programa que leia o nome completo de uma pessoa e mostre:
* O nome com todas as letras maiúsculas.
* O nome com todas as letras minúsculas.
* Quantas letras ao todo (sem considerar espaços).
* Quantas letras tem o primeiro nome.
'''

nome_completo = input('Digite o nome completo: ')
print(nome_completo.upper()) # Letras maiúsculas.
print(nome_completo.lower()) # Letras minúsculas.

sem_espacos = nome_completo.replace(' ', '') # Quantas letras ao todo (sem considerar espaços).
print(len(sem_espacos))

divide_nomes = nome_completo.split() # Quantas letras tem o primeiro nome.
print(len(divide_nomes[0]))
