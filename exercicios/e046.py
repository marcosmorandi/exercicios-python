'''
Exercício 046 - Feito
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''

from time import sleep
for cont in range(10 ,-1, -1): # "cont" é a variável de controle. Os dois primeiros números são a contagem, o terceiro é o passo.
    print(cont)
    sleep(1)
print('BUM! BUM! POOW!')
