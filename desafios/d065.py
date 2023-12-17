'''
Desafio 065 - Feito
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
média entre todos os valores e qual foi o maior e o menor valor lido.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

novo_valor = 's'
numero = 0
media = 0
maior = 0
menor = 9999
cont = 0
soma = 0
while novo_valor == 's':
    numero = int(input('Digite um número inteiro: '))
    cont += 1
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    soma += numero
    media = soma / cont
    novo_valor = str(input('Quer continuar digitando valores [S/N]: ')).lower()
print(f'Foram digitados {cont} números. O maior valor digitado foi {maior} o menor valor digitado foi {menor} e a média é {media}.')
