'''
Desafio 020 - Feito
O mesmo professor do desafio anterior quer sortear a ordem de apresentação...
de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos...
e mostre a ordem sorteada.
'''

# Importando a biblioteca "random".
import random

# Lendo o nome dos 4 alunos e criando a lista.
aluno1 = str(input('Nome do aluno 1: '))
aluno2 = str(input('Nome do aluno 2: '))
aluno3 = str(input('Nome do aluno 3: '))
aluno4 = str(input('Nome do aluno 4: '))
lista = [aluno1, aluno2, aluno3, aluno4]

# Escolhendo a ordem dos nomes de modo aleatório da lista.
random.shuffle(lista)

# Exibindo lista na tela.
print(f'Ordem de apresentação {lista}.')
