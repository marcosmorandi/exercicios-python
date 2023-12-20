'''
Exercício 065 - Feito
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
média entre todos os valores e qual foi o maior e o menor valor lido.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

resp = 'S'
soma = quant = media = 0 # Quando várias variáveis começam com o mesmo número, 0 no caso, pode se colocar na mesma linha.
while resp in 'Ss': # Quando várias variáveis começam com o mesmo número, 0 no caso, pode se colocar na mesma linha.
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num # Se for digitado apenas um número, o maior e menor serão esse número.
    else: # Depois do primeiro numero ele começa a comparar para colocar o maior e menor nas suas respectivas posições.
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0] # Joga para maiúsculas, remove espaços e só considera a primeira letra.
media = soma / quant # O cálculo da média funciona dentro ou fora do "while".
print(f'Você digitou {quant} números e a média foi {media}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
