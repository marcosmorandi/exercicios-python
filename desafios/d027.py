'''
Desafio 027 - Feito
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
Primeiro = Ana
Último = Souza
'''

nome_inteiro = str(input('Digite um nome: ')).strip() # Tira espaços vazios antes e depois da string.
nome_separado = nome_inteiro.split() # Separa o nome e da nova indexação para a string.
print(f'O primeiro nome é {(nome_separado[0])}.') # Primeira posição do nome.
print(f'O último nome é {(nome_separado[len(nome_separado)-1])}.') # Explicação abaixo.

'''
Na linha 12, O "len" percorre a string numerando de 0 até + 1 após o final, o "-1" remove o último espaço vazio e exibe a posição ou mostra a última letra de fato.

Ex:
-----
nome = str(input('Digite um nome: ')).strip()
print(f'A última posição do nome é {(len(nome))}.')
print(f'E é a letra {(nome[len(nome)])}.')

Digite um nome: ana
              # 0123
A última posição do nome é 3.
!!! IndexError: string index out of range !!! # Não tem letra na posição 3.
-----
nome = str(input('Digite um nome: ')).strip()
print(f'A última posição do nome é {(len(nome))}.')
print(f'E é a letra {(nome[len(nome)-1])}.')

Digite um nome: ana
              # 0123
A última posição do nome é 3.
E é a letra a. # 0123 -1 =2 que é a letra "a" na posição "2".
-----
'''
