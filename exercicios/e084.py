'''
Exercício 084 - Feito
Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista.
No final mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com a(s) pessoa(s) mais pesada(s).
C) Uma listagem com a(s) pessoa(s) mais leve(s).
'''

temp = [] # Lista temporária.
princ = [] # Litsa principal.
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1] # Temp na 0 é nome, temp na 1 é peso.
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:]) # Criando uma cópia.
    temp.clear() # Limpando o temp.
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
#print(f'Os dados foram {princ}') # Teste, ok.
print(f'Ao todo, você cadastrou {len(princ)} pessoas.') # Mostra o tamanho do cadastro principal.
print(f'O maior peso foi de {mai} Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='') # "{}" delimitador de interpolação.
print()
print(f'O menor peso foi de {men} Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='') # "{}" delimitador de interpolação.
print()
