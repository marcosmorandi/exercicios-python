'''
Desafio 004 - Feito
Faça um programa que leia algo pelo teclado,
mostre na tela o seu tipo primitivo
e todas as informações possiveis sobre ele.
'''

i = input('Digite algo: ') # "input" sem nada definido antes será considerado string.
print('O tipo primitivo desse valor é', type(i)) # Verifica o tipo primitivo.
print('Só tem espaços?', i.isspace()) # Verifica se só tem espaços.
print('É um número?', i.isnumeric()) # Verifica se é só número.
print('É alfabético?', i.isalpha()) # Verifica se é só alfabético, só letras.
print('É alfanumérico?', i.isalnum()) # Verifica se é alfanumérico, só letras e números.
print('Está em maiúsculas?', i.isupper()) # Verifica se está tudo em maiúsculas.
print('Está em minúsculas?', i.islower()) # Verifica se está tudo em minúsculas.
print('Está capitalizada?', i.istitle()) # Verifica se a letra inicial é maiúscula.
