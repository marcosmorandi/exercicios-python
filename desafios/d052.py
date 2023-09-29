'''
Desafio 052 - !bug - do 29 em diante ele não reconhece como primo!
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
Número primo: Divisível apenas por 1 e por ele mesmo)
'''

def primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    for c in range(5, int(numero ** 0.5) + 1, 6):
        if numero % 1 == 0 or numero % (c + 2) == 0:
            return False
    return True

try:
    numero = int(input('Digite um número inteiro: '))
    if primo(numero):
        print(f'{numero} é um número primo.')
    else:
        print(f'{numero} não é um número primo.')
except ValueError:
    print('Por favor, insira um número inteiro válido.')
