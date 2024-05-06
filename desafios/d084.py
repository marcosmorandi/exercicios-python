'''
Desafio 084 - Feito
Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista.
No final mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com a(s) pessoa(s) mais pesada(s).
C) Uma listagem com a(s) pessoa(s) mais leve(s).
'''

nome_peso = list() # Lista temoporária.
dados = list() # Lista principal
leves = pesadas = 0 # Mais leves e mais pesados iniciando com 0.
while True:
    nome_peso.append(str(input('Nome: '))) # Pegando o nome.
    nome_peso.append(float(input('Peso: '))) # Pegando o peso.
    if len(dados) == 0: # Se etiver na posição 0 da lista dados...
        leves = pesadas = nome_peso[1] # ...leves e pesados recebem o valor. nome_peso na 0 é nome, nome_peso na 1 é peso.
    else: # Se não estiver na posição 0...
        if nome_peso[1] > pesadas: # ...compara valores e ve se é o mais pesado...
            pesadas = nome_peso[1] # ...se for a variável pesados recebe o valor.
        if nome_peso[1] < leves: # Faz a mesma comparação com o mais leve.
            leves = nome_peso[1]
    dados.append(nome_peso[:]) # Criando uma cópia.
    nome_peso.clear() # Limpando a temporária.
    resposta = ' '
    while resposta not in 'sn': # Enquanto a resposta não for S ou N fica perguntando.
        resposta = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if resposta == 'n': # Se for N para.
        break
print(f'Dados digitados foram {dados}.') # Testes se os dados foram armazenados.
print(f'A) Ao todo foram cadastradas {len(dados)} pessoas.') # Mostra o tamanho do cadastro principal.
print(f'B) O maior peso foi de {pesadas} Kg. Peso de ', end='') # Mostra o maior peso...
for pessoas in dados: # ...e cria um laço para imprimir quem ficou com o maior ou maiores pesos.
    if pessoas[1] == pesadas:
        print(f'[{pessoas[0]}] ', end='')
print(f'\nC) O menor peso foi de {leves} Kg. Peso de ', end='') # Mostra o menor peso...
for pessoas in dados: # ... e cria outro laço para imprimir o ou os mais leves.
    if pessoas[1] == leves:
        print(f'[{pessoas[0]}]', end='')
