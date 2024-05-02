'''
Desafio 080 - Feito
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final mostre a lista ordenada na tela.
'''

lista = []
for c in range(0, 5):
    numero = int(input('Digite um valor: '))
    if c == 0 or numero > lista[-1]: # Se for o primeiro ou maior que o último da lista...
        lista.append(numero) # ...dar um append.
        print('Adicionado ao final da lista...') # Informa a que posição foi adicionado.
    else:
        posicao = 0
        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                print(f'Adicionado na posição {posicao} da lista.')
                break
            posicao += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
