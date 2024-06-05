'''
Exercício 085 - Feito
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
seperados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''

num = [[], []] # 1 lista onde dentro dessa lista tem 2 listas internas.
valor = 0
for contador in range(1, 8):
    valor = int(input(f'Digite o {contador}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
#print(f'Todos os valores: {num}') # Teste de todos os valores digitados.
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}') # 0 grupo dos pares.
print(f'Os valores ímpares digitados foram: {num[1]}') # 1 grupo dos ímpares.
