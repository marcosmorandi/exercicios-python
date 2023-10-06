'''
Exercício 047 - Feito
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
'''

# É sempre preferível fazer algoritmos que exijam menos das máquinas.
for n in range(2, 51, 2):
    print('.', end='') # Aqui mostra a quantidade de laços de repetição, 1, metade da solução abaixo, o que economiza processamento.
    print(n, end=' ') # O "end=''" serve para deixar tudo na mesma linha.
print('Acabou')

# A solução abaixo também funciona, mas será feito 2 laços de repetição para cada resultado, aumentando o processamento.
'''
for n in range(1, 51):
    print('.', end='') # Mosta os laços de repetição, nesse caso 2.
    if n % 2 == 0:
        print(n, end=' ') # O "end=''" serve para deixar tudo na mesa linha.
print('Acabou')
'''
