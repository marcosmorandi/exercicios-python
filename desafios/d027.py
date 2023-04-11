'''
Desafio 027 - Incorreto, ver aula
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
Primeiro = Ana
Último = Souza
'''

nome_completo = input(str('Digite o nome completo: '))

primeiro_nome = nome_completo.split()

ultimo_nome = nome_completo.split()

print(f'Primeiro nome: {primeiro_nome[0]}')
print(f'Ultimo nome: {ultimo_nome[:]}')
