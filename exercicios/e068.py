'''
Exercício 068 - Feito
Faça um programa que jogue par ou ímpar com o computador.
O jogo será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que
ele conquistou no final do jogo.
'''

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' ' # Inicializa a variável "tipo" com uma string vazia.
    while tipo not in 'PI': # Enquanto não for digitado 'P' ou 'I', o programa contina perguntando.
        tipo = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0] # "strip" remove espaços vazios do começo e final, "upper" deixa maiúsculo, "[0]" pega só a primeira letra.
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
