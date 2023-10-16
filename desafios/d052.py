'''
Desafio 052 - Feito
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
Número primo: Divisível apenas por 1 e por ele mesmo)
'''

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='') # Amarelo se divisível.
        tot += 1 # Versão simplificada de "tot = tot + 1".
    else:
        print('\033[31m', end='') # Vermelho se não divisível.
    print(f'{c}', end=' ') # Imprime na mesma linha todos os números do laço de repetição.
print(f'\n\033[mO número {num} foi divisível {tot} vezes.') # "\n" para quebrar a linha e "\033[m" para voltar a cor branca padrão.
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
