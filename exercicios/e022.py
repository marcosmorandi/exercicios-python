'''
Exercício 022 - Feito
Crie um programa que leia o nome completo de uma pessoa e mostre:
* O nome com todas as letras maiúsculas.
* O nome com todas as letras minúsculas.
* Quantas letras ao todo (sem considerar espaços).
* Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite o nome completo: ')).strip() # "strip" elimina os espaços antes e depois, não entre as palavras.
print('Analisando o nome...')
print(f'O nome em maiúsculas é {(nome.upper())}.')
print(f'O nome em minúsculas é {(nome.lower())}.')
print(f'O nome tem ao todo {(len(nome) - nome.count(" "))} letras.') # Conta as letras eliminando os espaços da contagem.
print(f'O primeiro nome tem {(nome.find(" "))} letras.') # Conta as letras até o primeiro espaço.
print('(Outra forma de contar as letras do primeiro nome.)')
separa = nome.split() # Separa o nome em strings individuais.
print(f'O primeiro nome é {(separa[0])} e ele tem {len(separa[0])} letras.') # Mostra o primeiro nome "0" e quantidade de letra dele "len(separa[0])".
