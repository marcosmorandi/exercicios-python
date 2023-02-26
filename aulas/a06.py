'''
Tipos primitivos mais básicos que existem
"int": Números inteiros. 7, -4, 0, 9875
"float": Números reais, ou números de ponto flutuante. 4.5, 0.076, -15.223, 7.0 (Python e o padrão internacional usa "." para separar numeros reais, no BR se usa ",".)
"bool": Valores lógicos, booleanos, verdadeiro ou falso. True (verdadeiro), False (falso), a primeira letra sempre maiúscula.
"str": Valores caractere ou strings. Palavras, 'Olá', '7.5' (nesse caso é palavra), '' (string vazia).
'''

# Verificando o tipo primitivo.
n1 = int(input('Digite um valor: '))
print(type(n1))

print('')

# Verificando se é número.
n = input('Digite algo: ')
print(n.isnumeric())

print('')

# Verificando se é letra.
n = input('Digite algo: ')
print(n.isalpha())

print('')

# Verificando se é alfa-numérico.
n = input('Digite algo: ')
print(n.isalnum())

print('')

# Verificando se é maiúscula.
n = input('Digite algo: ')
print(n.isupper())
