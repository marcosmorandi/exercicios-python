'''
Exercício 004 - Feito
Faça um programa que leia algo pelo teclado,
mostre na tela o seu tipo primitivo
e todas as informações possiveis sobre ele.
Agora usando o format.
'''

i = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(i)))
print(f'Só tem espaços? {i.isspace()}') # Outra forma para o ".format", quando o de cima não funcionar.
print(f'É um número? {i.isnumeric()}')
print(f'É alfabético? {i.isalpha()}')
print(f'É alfanumérico? {i.isalnum()}')
print(f'Está em maiúsculas? {i.isupper()}')
print(f'Está em minúsculas? {i.islower()}')
print(f'Está capitalizada? {i.istitle()}')
