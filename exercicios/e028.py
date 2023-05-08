'''
Exercício 028 - Feito
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint
from time import sleep # Para usar o "sleep".
computador = randint(0, 5) # Faz o computador sortear.
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta advinhar.
print('Processando...')
sleep(3) # Cria uma expectativa no jogo, pois demora o tempo em segundos antes de partir para o próximo comando.
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print(f'Ganhei! Eu pensei no número {computador} e não no {jogador}!')
