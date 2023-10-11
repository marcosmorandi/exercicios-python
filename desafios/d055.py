'''
Desafio 055
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor
peso lido.
'''

maior_peso = 0
menor_peso = 0

for c in range(1, 6):
    peso = float(input(f'Digite o peso da pessoa {c}: '))
    
