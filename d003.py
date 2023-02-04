'''
Desafio 003 - Feito
Crie um programa que leia dois números e tente mostrar a soma entre eles.
Exemplo:
"Primeiro número: 6"
"Segundo número: 3"
"A soma é 63 (errado, o certo é 9)"
Juntar uma string na outra é concatenação, somar não é concatenar.
'''

# 1ª forma
p_num = int(input('Primeiro número: ')) # Quando se abre um "input" sem difinir nada antes, o Python assume que é string, nesse caso a soma não daria certo.
s_num = int(input('Segundo número: ')) # "int" funciona melhor para números inteiros do que "float".
print('A soma é:', (p_num + s_num)) # Aqui o "+" não funciona, pois não se pode concatenar com "+" str com int, tem que usar ",".

print('')

# 2ª forma
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
print('A soma vale', s)

print('')

# 3ª forma
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
soma = n1 + n2
print('A soma vale: {}'.format(soma))

print('')

# 4ª forma
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
soma = n1 + n2
print('A soma entre', n1 , 'e', n2 , 'vale {}.'.format(soma)) # Com a "," no final ficava um espaço entre o número da soma e o ".".

print('')

# 5ª forma
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
soma = n1 + n2
print('A soma entre {} e {} vale {}.'.format(n1, n2, soma)) # A forma máis prática de representar.
