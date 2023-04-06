'''
Desafio 025 - Feito
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''

nome = input(str('Digite seu nome: '))

nome.split()

if ('Silva' in nome.split()) or ('silva' in nome.split()) or ('SILVA' in nome.split()):
    print('Tem "Silva" no nome!')
else:
    print('Não tem "Silva" no nome!')
