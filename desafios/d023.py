'''
Desafio 023 - Feito
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
Ex:
Digite um número: 1834
Unidade: 4
Dezena: 3
Centenas: 8
Milhar: 1
'''
numero = input(str('Digite um número de 0 a 9999: '))
print(f'Unidade: {numero[3]}')
print(f'Dezena: {numero[2]}')
print(f'Centena: {numero[1]}')
print(f'Milhar: {numero[0]}')
