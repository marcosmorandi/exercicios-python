'''
Desafio 087 - Feito
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = somaterceiracoluna = maiorsegundalinha = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='') # ":^5" formata o valor centralizado e com 5 casa decimais.
        if matriz[linha][coluna] % 2 == 0:
            somapares += matriz[linha][coluna]
    print() # Para quebrar a linha depois de 3 valores.
print(f'A) A soma de todos valores pares é {somapares}.')
for linha in range(0, 3):
    somaterceiracoluna += matriz[linha][2]
print(f'B) A soma dos valores da terceira coluna é {somaterceiracoluna}.')
for coluna in range(0, 3):
    if coluna == 0:
        maiorsegundalinha = matriz[1][coluna]
    elif matriz[1][coluna] > maiorsegundalinha:
        maiorsegundalinha = matriz[1][coluna]
print(f'C) O maior valor da segunda linha é {maiorsegundalinha}.')
