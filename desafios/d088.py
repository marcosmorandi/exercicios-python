'''
Desafio 088 - Feito
Faça um programa que ajude um jogador da Mega Sena a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''

from random import randint # Da biblioteca random importa o randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('      JOGO DA MEGA SENA      ')
print('-' * 30)
quantidadejogos = int(input('Quantos jogos serão gerados: '))
total = 1 # Se não o jogo 1 fica jogo 0 na contagem e pedindo 5 jogos aparecem 6.
while total <= quantidadejogos:
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista: # Se o número não está na lista, ele será adicionado.
            lista.append(numero)
            contador += 1
        if contador >= 6:
            break
    lista.sort() # Ordem crescente.
    jogos.append(lista[:]) # Cria cópia da lista.
    lista.clear() # Apaga a lista.
    total += 1
print('-=' * 3, f'SORTEANDO {quantidadejogos} JOGOS ', '-=' * 3)
for i, l, in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-' * 5, '< BOA SORTE! >', '-=' * 5)
