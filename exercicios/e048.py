'''
Desafio 048 - Feito
Faça um programa que calcule a soma entre todos os números impares que são multiplos de três
e que se encontram no intervalo de 1 até 500.
'''

soma = 0 # Conceito de acumulador.
cont = 0 # Contador.
impares = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1 # Conta os valores que atendem o que foi especificado. Pode ser simplificado com "soma += c".
        soma = soma + c # "soma" recebe o que ela tem mais o número.
    impares = impares + 1 # Conta número ímpares ao todo. Note que basou mudar a indentação para um resultado diferente.
print(f'A soma de todos os {cont} valores solicitados é {soma}, mas entre 1 e 500 existem {impares} números ímpares.')
