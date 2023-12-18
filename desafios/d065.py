'''
Desafio 065 - Feito
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
média entre todos os valores e qual foi o maior e o menor valor lido.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

valor = 's'
soma = contador = media = maior = menor = 0 # Quando várias variáveis começam com o mesmo número, 0 no caso, pode se colocar na mesma linha.
while valor in 'Ss': # Enqunto o valor estiver em S maiúsculo ou minúsculo.
    numero = int(input('Digite um número inteiro: '))
    contador += 1
    soma += numero
    if contador == 1:
        maior = menor = numero # Se for digitado apenas um número, o maior e menor serão esse número.
    else: # Depois do primeiro numero ele começa a comparar para colocar o maior e menor nas suas respectivas posições.
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    media = soma / contador # O cálculo da média funciona dentro ou fora do "while".
    valor = str(input('Quer continuar digitando valores [S/N]: ')).upper().strip()[0] # Joga para maiúsculas, remove espaços e só considera a primeira letra.
print(f'Foram digitados {contador} número(s).')
print(f'O maior valor digitado foi {maior}, o menor valor digitado foi {menor} e a média entre ele é {media}.')
