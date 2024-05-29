'''
Exercício 078 - Feito
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitados e as suas respectivas posiçõs na lista.
'''

listanum = []
mai = 0
men = 0
for c in range(0, 5): # 0 ao 4, 5 é descartado.
    listanum.append(int(input(f'Digite um valor para a psoição {c}: ')))
    if c == 0: # Quando foi o primeiro valor lido...
        mai = men = listanum[c] # ...ele é o maior e o menor.
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} na(s) posição(ões) ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men} na(s) posição(ões) ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
print()
