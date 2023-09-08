'''
Desafio 046 - Feito
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''

from time import sleep # Importanto a pausa de 1 segundo.
for c in range(10, -1, -1): # "c" de variável de controle, ou contador. Primeiro "-1" para exibir até o número anterior (0). Segundo "-1" para contagem regressiva de 1 em 1.
    print(c)
    sleep(1) # Pausa de 1 segundo.
print('Estourando fogos!')
