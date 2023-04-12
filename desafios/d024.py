'''
Desafio 024 - Feito
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
'''

cidade = input(str('Digite o nome de uma cidade: '))

cidade.split()

if ('Santo' in cidade.split()[0]) == True:
    print('Essa cidade começa com o nome "Santo"!')
elif ('SANTO' in cidade.split()[0]) == True:
    print('Essa cidade começa com o nome "Santo"!')
elif ('santo' in cidade.split()[0]) == True:
    print('Essa cidade começa com o nome "Santo"!')
else:
    print('Essa cidade não começa com o nome "Santo"!')
