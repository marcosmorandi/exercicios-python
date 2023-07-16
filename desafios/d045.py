'''
Desafio 045 - Feito
Crie um programa que faça o computador jogar Jokempô(pedra, papel, tesoura) com você.
'''

from random import randint

print('{:=^40}'.format(' Jokempô '))
print('{:=^40}'.format(' Pedra Papel Tesoura '))

escolha_computador = randint(1, 3)
escolha_jogador = int(input('''Escolha:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
  '''))

if escolha_jogador != 1 and escolha_jogador != 2 and escolha_jogador != 3:
    print('Opção inválida, tente denovo.')
else:
    print(f'Você escolheu {escolha_jogador}.')
    if escolha_jogador == 1:
        print('[1 - Pedra]')
    elif escolha_jogador == 2:
        print('[2 - Papel]')
    elif escolha_jogador == 3:
        print('[3 - Tesoura]')
    print(f'O computador escolheu {escolha_computador}.')
    if escolha_computador == 1:
        print('[1 - Pedra]')
    elif escolha_computador == 2:
        print('[2 - Papel]')
    elif escolha_computador == 3:
        print('[3 - Tesoura]')

if escolha_jogador == escolha_computador:
    print('Ambos escolheram igual, empate.')
elif escolha_jogador == 1 and escolha_computador == 2:
    print('Jogador escolheu [1 - Pedra], computador escolheu [2 - Papel]. Computador ganhou.')
elif escolha_jogador == 1 and escolha_computador == 3:
    print('Jogador escolheu [1 - Pedra], computador escolheu [3 - Tesoura]. Jogador ganhou.')
elif escolha_jogador == 2 and escolha_computador == 1:
    print('Jogador escolheu [2 - Papel], computador escolheu [1 - Pedra]. Jogador ganhou.')
elif escolha_jogador == 2 and escolha_computador == 3:
    print('Jogador escolheu [2 - Papel], computador escolheu [3 - Tesoura]. Computador ganhou.')
elif escolha_jogador == 3 and escolha_computador == 1:
    print('Jogador escolheu [3 - Tesoura], computador escolheu [1 - Pedra]. Computador ganhou.')
elif escolha_jogador == 3 and escolha_computador == 2:
    print('Jogador escolheu [3 - Tesoura], computador escolheu [2 - Papel]. Jogador ganhou.')
