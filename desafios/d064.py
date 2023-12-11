'''
Desafio 064 - Feito
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é o condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''

numeros = 0
contador = 0
soma = 0
numeros = int(input('Digite um número inteiro para soma, para parar digite 999: '))
while numeros != 999:
    soma += numeros
    contador += 1
    numeros = int(input('Digite um número inteiro para soma, para parar digite 999: '))
print(f'Foram digitados {contador} números e a soma de todos eles é igual a {soma}.')
