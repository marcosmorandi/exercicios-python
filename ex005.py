'''
Exercicio 005 -
Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.
'''

n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o seu sucessor é {}.'.format(n, (n-1), (n+1)))
# Se futuramente não vai precisar da variáveis de novo, use o minimo possível para poupar memória.
