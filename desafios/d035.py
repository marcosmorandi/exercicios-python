'''
Desafio 035 - Não parece correto
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
ou não formar um triângulo.
'''
# Pesquise o principio matemático que diz se 3 retas podem ou não formar um triângulo.
# A regra é a seguinte: A soma de dois lados é sempre menor que o terceiro lado.

reta_1 = int(input('Digite o tamanho da primeira reta: '))
reta_2 = int(input('Digite o tamanho da segunda reta: '))
reta_3 = int(input('Digite o tamanho da terceira reta: '))

if ((reta_1 + reta_2) < reta_3) or ((reta_1 + reta_3) < reta_2) or ((reta_2 + reta_3) < reta_1):
    print('Essas medidas podem formar um triângulo.')
else:
    print('Essas medidas não podem formar um triângulo.')
