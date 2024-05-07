'''
Desafio 085 - Feito
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em
uma lista única que mantenha separados os valores pares e ímpares.
No final mostre os valores pares e ímpares em ordem crescente.
'''

lista = [[], []] # 1 lista que contém dentro 2 listas.
for contador in range(1, 8): # Pede valores do 1º ao 7º.
    numero = int(input(f'Digite o {contador}º valor: ')) # Pede os valores.
    if numero % 2 == 0: # Se for divisivel por 2 (par)...
        lista[0].append(numero) # ...coloca na lista "0" de pares.
    else: # Se não...
        lista[1].append(numero) #...na lista "1" de ímpares.
lista[0].sort() # Coloca a lista 0 de pares em ordem crescente.
lista[1].sort() # Coloca a lista 1 de ímpares em ordem crescente.
print(f'Os valores pares digitados foram: {lista[0]}') # Exibe a lista 0 de pares.
print(f'Os valores ímpares digitados foram: {lista[1]}') # Exibe a lista 1 de ímpares.
