'''
Desafio 081 - Feito
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

numeros = list()
while True:
    numeros.append(int(input('Digite um valor: ')))
    resposta = ' '
    while resposta not in 'sn': # Se a resposta não for "S" ou "N" ele vai ficar perguntando.
        resposta = str(input('Quer continuar? [S/N] ')).lower().strip() # Se necessário converte maiúscula para minúscula.
    if resposta == 'n':
        break
print(f'A) Você digitou {len(numeros)} números.')
numeros.sort(reverse=True)
print(f'B) Os números em ordem decrescente são {numeros}.')
if 5 in numeros:
    print('C) O número 5 está na lista.')
else:
    print('C) O número 5 não está na lista.')
