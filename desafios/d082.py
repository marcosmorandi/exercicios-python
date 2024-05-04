'''
Desafio 082 - Feito
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''

numeros = list()
pares = list()
impares = list()
while True:
    numeros.append(int(input('Digite um número: ')))
    resposta = ' '
    while resposta not in 'sn':
        resposta = str(input('Quer continuar? [S/N] ')).lower().strip()
    if resposta == 'n':
        break
for i, v, in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'A lista completa é {numeros}.')
print(f'A lista de pares é {pares}.')
print(f'A lista de ímpares é {impares}.')
