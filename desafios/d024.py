'''
Desafio 024 - Feito
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
'''
cidade = input(str('Digite o nome de uma cidade: '))

if ('Santo' in cidade) == True:
    print('Tem o nome "Santo" nessa cidade!')
elif ('SANTO' in cidade) == True:
    print('Tem o nome "Santo" nessa cidade!')
else:
    print('Não tem o nome "Santo" nessa cidade!')
