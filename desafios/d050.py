'''
Desafio 050
Desenvolva uma programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
'''

for c in range(1, 7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        soma = n + n
print(f'A soma dos números pares digitados é {n}.')
