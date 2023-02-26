'''
Desafio 019 - Feito
Um professor quer sortear um dos seus quatro alunos para apagar o quadro...
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''
# Dica: "random" aqui?

# Importando a biblioteca "random".
import random

# Lendo os 4 nomes e criando a lista de nomes de alunos.
aluno1 = str(input('Nome do aluno 1: ')) # João
aluno2 = str(input('Nome do aluno 2: ')) # Maria
aluno3 = str(input('Nome do aluno 3: ')) # Pedro
aluno4 = str(input('Nome do aluno 4: ')) # Ana
lista = [aluno1, aluno2, aluno3, aluno4]

# Escolhendo um nome aleatório.
nome_aleatorio = random.choice(lista)

# Exibindo o resultado na tela.
print(f'O aluno escolhido para apagar o quadro foi {nome_aleatorio}.')
print(f'Parabéns {nome_aleatorio}!')
