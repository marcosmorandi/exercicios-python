'''
Desafio 025 - Feito
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''

nome = str(input('Digite seu nome: ')).strip() # Remove espaços em branco antes e depois da string.

if ('silva' in nome.lower()) == True: # Independente de como o usuário digitar, deixa tudo em minúsculo e procura a palavra.
    print('Tem "Silva" no nome.')
else:
    print('Não tem "Silva" no nome.')
