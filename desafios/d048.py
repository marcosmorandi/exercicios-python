'''
Desafio 048 - Feito
Faça um programa que calcule a soma entre todos os números impares que são múltiplos de 
3 e que se encontram no intervalo de 1 até 500.
'''

# Resultado é 20.667

soma = 0 # Variável soma começa zerada.

for c in range(1, 501): # Intervalo de 1 a 500 (501 não será mostrado).
    if c % 2 != 0 and c % 3 == 0: # Resto da divisão por 2 diferente de 0 é impar. Resto da divisão por 3 igual a 0 é múltiplo de 3.
        soma += c # Se atende a condição acima então soma.
print(f'A soma dos números ímpares múltiplos de 3 entre 1 e 500 é {soma}') # Imprime o resultado.
