'''
Desafio 079 - Feito
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores
únicos digitados, em ordem crescente.
'''

lista = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, descartado!')
    resposta = ' '
    while resposta not in 'sn': # Se a resposta não for "S" ou "N" ele vai ficar perguntando.
        resposta = str(input('Quer continuar? [S/N] ')).lower().strip() # Se necessário converte maiúscula para minúscula.
    if resposta == 'n':
        break
print('-=' * 30)
lista.sort()
print(f'Os valores digitados em ordem crescente foram {lista}')
print('-=' * 30)
