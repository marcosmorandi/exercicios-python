'''
Exercício 051 - Feito
Desenvolva um programa que leia o primeiro termo e a razão de uma PA(progressão aritmética).
No final, mostre os 10 primeiros termos dessa progressão.
'''

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 -1) * razao # Fórmula do enésimo termo de uma PA.
for c in range(primeiro, decimo + razao, razao):
    print(f'{c}', end=' -> ')
print('Acabou')
