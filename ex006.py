'''
Desafio 006 -
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''

# Com 3 variáveis:
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)

print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r)) # A mesma variável pode aparecer mais de uma vez no mesmo print.
print('')

# Com uma única variável:
n = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, (n**(1/2)))) # A mesma variável pode aparecer mais de uma vez no mesmo print.
print('')

# Outra forma de calcular a raiz quadrada:
n = int(input('Digite um número: '))
print('A raiz quadrada de {} é igual a {:.2f}.'.format(n, pow(n, (1/2)))) # "pow" função power, de potência.
print('')
