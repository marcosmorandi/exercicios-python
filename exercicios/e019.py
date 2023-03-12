'''
Exercício 019
Um professor quer sortear um dos seus quatro alunos para apagar o quadro...
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''

from random import choice # Ou "import random";
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4] # Qualquer tipo de lista fica entre colchetes "[]".
escolhido = choice(lista) # Se usado "import randon" aqui fica "escolhido = randon.choice(lista)".
print(f'O aluno escolhido foi {escolhido}.')
