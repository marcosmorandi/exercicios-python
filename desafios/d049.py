'''
Desafio 049 - Feito
Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço "for".
'''

numero = int(input('Digite um número para ver sua tabuada: ')) # Recebe o número.
for c in range (0, 11): # Laço de repetição de 0 a 10.
    print(numero, 'X', c, '=', numero * c) # Imprime número + "X" + o número da repetição + "=" e o resultado.
