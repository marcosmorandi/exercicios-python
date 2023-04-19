'''
Desafio 027 - (Tentar refazer com o strip e split juntos)
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
Primeiro = Ana
Último = Souza
'''

nome_inteiro = str(input('Digite um nome: ')).strip() # Tira espaços vazios antes e depois da string.
nome_separado = nome_inteiro.split() # Separa o nome e da nova indexação para a string.
print(f'O primeiro nome é {(nome_separado[0])}.') # Primeira posição do nome.
print(f'O último nome é {(nome_separado[len(nome_separado)-1])}.')

# ver comentários aqui para entender o -1 https://www.youtube.com/watch?v=SifYYsXhLM8&t=404s
