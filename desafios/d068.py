'''
Desafio 068 - Feito
Faça um programa que jogue par ou ímpar com o computador.
O jogo será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que
ele conquistou no final do jogo.
'''

# Exemplo:
# =-=-=-=-=-=-=-=-=-=-=-=-=
# Vamos jogar par ou ímpar
# =-=-=-=-=-=-=-=-=-=-=-=-=
# Diga um valor: 8
# Par ou Ímpar? [P/I] p
# -------------------------
# Voce jogou 8 e o computador 2. Total de 10, DEU PAR
# -------------------------
# Você VENCEU!
# Vamos jogar novamente...
# =-=-=-=-=-=-=-=-=-=-=-=-=
# Diga um valor: 8
# ou
# =-=-=-=-=-=-=-=-=-=-=-=-=
# Vamos jogar par ou ímpar
# =-=-=-=-=-=-=-=-=-=-=-=-=
# Diga um valor: 6
# Par ou Ímpar? [P/I] i
# -------------------------
# Voce jogou 6 e o computador 10. Total de 16, DEU PAR
# -------------------------
# Você PERDEU!
# =-=-=-=-=-=-=-=-=-=-=-=-=
# GAME OVER! Você venceu 0 vezes.

from random import randint
from time import sleep

venceu = 0
while True:
    print('=-' * 20)
    print('Vamos jogar par ou ímpar')
    print('=-' * 20)
    n_jogador = int(input('Diga um valor: '))
    p_i = str(input('Par ou Ímpar?[P/I]: ')).lower()
    n_computador = randint(0, 10)
    soma = n_jogador + n_computador
    print('-' * 20)
    if soma % 2 == 0:
        print(f'Você jogou {n_jogador} e o computador {n_computador}. Total de {soma}, DEU PAR!')
        print('-' * 20)
        if p_i == 'p':
            print('Você VENCEU!')
            venceu += 1
            print('Vamos jogar novamente...')
            sleep(3)
        else:
            break
    elif soma % 2 != 0:
        print(f'Você jogou {n_jogador} e o computador {n_computador}. Total de {soma}, DEU ÍMPAR!')
        print('-' * 20)
        if p_i == 'i':
            print('Você VENCEU!')
            venceu += 1
            print('Vamos jogar novamente...')
            sleep(3)
        else:
            break
print('Você PERDEU!')
print(f'GAME OVER! Você venceu {venceu} vez(es).')
