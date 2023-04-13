'''
Exercício 022 - Feito
Crie um programa que leia o nome completo de uma pessoa e mostre:
* O nome com todas as letras maiúsculas.
* O nome com todas as letras minúsculas.
* Quantas letras ao todo (sem considerar espaços).
* Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite o nome completo: ')).strip()
print('Analisndo o nome...')
print(f'O nome em maiúsculas é {(nome.upper())}.')
print(f'O nome em minúsculas é {(nome.lower())}.')
print(f'O nome tem ao todo {(len(nome) - nome.count(" "))} letras.')
print(f'O primeiro nome tem {(nome.find(" "))} letras.')
