'''
Desafio 03 - Concluido!
Crie um programa que leia dois números e tente mostrar a soma entre eles.
Exemplo:
"Primeiro número: 6"
"Segundo número: 3"
"A soma é 63 (errado, o certo é 9)"
'''

p_num = int(input('Primeiro número: ')) # "int" funciona melhor para número inteiros do que "float".
s_num = int(input('Segundo número: '))
print('A soma é:', (p_num + s_num)) # Aqui o "+" não funciona, pois não se pode concatenar com "+" str com int, tem que usar ",".
