'''
Desafio 078 - Feito
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitados e as suas respectivas posiçõs na lista.
'''

valores = list() # Outra forma de criar a lista vazia. "list()" ou "[]".
maior = 0 # Inicializando o menor valor com 0.
menor = 0 # Inicializando o maior valor com 0.
for c in range(0, 5): # 0 ao 4, 5 é descartado.
    valores.append(int(input('Digite um valor: '))) # Lendo os valores.
    if c == 0: # Quando foi o primeiro valor lido...
        maior = menor = valores[c] # ...ele é o maior e o menor.
    else: # Senão...
        if valores[c] > maior: # ...se o valor digitado for o maior...
            maior = valores[c] # ...o maior vai receber o valor digitado...
        if valores[c] < menor: # Se o valor digitado foi o menor...
            menor = valores[c] # ...o menor recebe o valor digitado.
for c, v, in enumerate(valores):
    print(f'Na posição {c} foi digitado o valor {v}.')
print(f'\nO maior valor digitado foi {max(valores)} na(s) posição(ões) ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i} ', end='')
print(f'\nO menor valor digitado foi {min(valores)} na(s) posição(ões) ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i} ', end='')
