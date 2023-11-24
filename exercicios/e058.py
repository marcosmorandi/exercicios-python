'''
Exercício 058 - Feito
Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer.
'''

# Desafio 028 - Feito
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
# para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

# import random # Biblioteca que gera o número aleatório.
# numero_aleatorio = random.randint(0,5) # A variável é definida usando o método "randint" da biblioteca "random", que gera um número inteiro aleatório entre 0 e 5.
# palpite = int(input('Tente advinhar o número gerado pelo computador, de 0 a 5: ')) # Lê o palpite do usuário.
# if palpite == numero_aleatorio: # Se o palpite for igual o numero aleatório:
#     print(f'Número gerado {numero_aleatorio}, seu palpite {palpite}. Parabéns, acertou!')
# else: # Senão:
#     print(f'Número gerado {numero_aleatorio}, seu palpite {palpite}. Que pena, errou!')

from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
acertou = False # Variável booleana que recebe "True" ou "False" para verdadeiro ou falso.
palpites = 0
while not acertou: # O laço de repetição será feito enquanto não acertar, ou seja enquanto o "acertou" continuar "False".
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True # Se cair nesse "if", aqui acaba o laço de repetição.
    else: # Senão aqui continua.
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')
