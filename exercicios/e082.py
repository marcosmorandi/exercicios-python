'''
Exercício 082 - Feito
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''

num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite uma número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'nN':
        break
for i, v, in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('=-' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista ímpares é {impares}')
