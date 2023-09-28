'''
Desafio 051 - Feito
Desenvolva um programa que leia o primeiro termo e a razão de uma PA(progressão aritmética).
No final, mostre os 10 primeiros termos dessa progressão.
'''

# Solicita ao usuário que insira o primeiro termo (a1) e a razão (r).
a1 = float(input('Digite o primeiro termo da progressão aritmética: '))
r = float(input('Digite a razão da progressão aritmética: '))

# Inicializa um lista para armazenar os 10 primeiros termos da progressão.
progressao_aritmetica = []

# Calcula e adiciona os 10 primeiros termos a lista.
for c in range(10):
    termo = a1 + c * r
    progressao_aritmetica.append(termo)

# Mostra os 10 primeiros termos da progressão.
print('Os 10 primeiros termos da progressão aritmética são:')
for termo in progressao_aritmetica:
    print(termo)
