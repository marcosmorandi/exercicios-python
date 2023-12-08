'''
Desafio 063 - Feito
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos
de uma Sequência de Fibonacci.
Ex:
0 > 1 > 1 > 2 > 3 > 5 > 8
'''

numero = int(input('Digite um número inteiro para a Sequência de Fibonacci: '))

a, b = 0, 1 # Inicializa as variáveis para os dois primeiros elementos da sequência.

contador = 0

while contador < numero: # Imprime ate a numero definido.
    print(a, end=' ')
    a, b = b, a + b
    contador += 1
