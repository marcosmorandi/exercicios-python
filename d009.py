'''
Desafio 009 - Feito
Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.
'''

numero = int(input('Digite um número inteiro: '))

for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)
