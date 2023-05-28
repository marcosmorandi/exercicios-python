'''
Desafio 035 - Feito
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
ou não formar um triângulo.
'''

# Pesquise o principio matemático que diz se 3 retas podem ou não formar um triângulo.
# A regra é a seguinte: Cada um dos segmentos tem que ser menor que a soma do comprimento dos outros dois.

reta_1 = float(input('Digite o tamanho da primeira reta: '))
reta_2 = float(input('Digite o tamanho da segunda reta: '))
reta_3 = float(input('Digite o tamanho da terceira reta: '))

if ((reta_1 + reta_2) > reta_3) and ((reta_1 + reta_3) > reta_2) and ((reta_2 + reta_3) > reta_1):
    print('Essas medidas podem formar um triângulo.')
else:
    print('Essas medidas não podem formar um triângulo.')
