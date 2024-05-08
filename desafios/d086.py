'''
Desafio 086 - Feito
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
Exemplo:
[1][2][3]
[4][5][6]
[7][8][9]
'''

matriz = [[0,0,0], [0,0,0], [0,0,0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='') # ":^5" formata o valor centralizado e com 5 casa decimais.
    print() # Para quebrar a linha depois de 3 valores.
