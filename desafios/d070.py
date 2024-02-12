'''
Desafio 070 - Feito
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o 
usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000,00.
C) Qual é o nome do produto mais barato.
'''

# --------------------
#  Loja Super Baratão
# --------------------
# Nome do produto: Mouse
# Preço: R$ 50
# Quer continuar? [S/N] y
# Quer continuar? [S/N] s
# Nome do produto: Caneta
# Preço: R$ 3
# Quer continuar? [S/N] n
# ----- Fim do Programa -----
# O total da compra foi R$ 53.00
# Temos 0 produto(s) custando mais de R$ 1000.00
# O produto mais barato foi Caneta que custa R$ 3.00

total_compra = mais_mil = v_mais_barato = contador = 0
p_mais_barato = ' '
print('-'*20)
print(' Loja Super Baratão ')
print('-'*20)
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    contador += 1
    total_compra += preco
    if preco > 1000:
        mais_mil += 1
    if contador == 1 or preco < v_mais_barato:
        v_mais_barato = preco
        p_mais_barato = produto
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if continua == 'N':
        break
print('-'*5 + ' Fim do Programa ' + '-'*5)
print(f'O total da compra foi R$ {total_compra:.2f}')
print(f'Temos {mais_mil} produto(s) custando mais de R$ 1000.00')
print(f'O produto mais barato foi {p_mais_barato} que custa R$ {v_mais_barato:.2f}')
