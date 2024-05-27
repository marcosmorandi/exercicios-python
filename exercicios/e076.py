'''
Exercício 076 - Feito
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-' * 39)
print(f'{"LISTAGEM DE PRECOS":^39}') #":^39" 39 espaços e centralizado.
print('-' * 39)
for pos in range(0, len(listagem)):
    if pos % 2 == 0: # Se par mostra o nome do item.
        print(f'{listagem[pos]:.<30}', end='') # ":.<30" alinhado texto a esquerda e prenchido até o espaço 30 com pontinhos.
    else: # Se não mostra o preço.
        print(f'R${listagem[pos]:>7.2f}') # ":>7.2f" alinhando a direita, 7 espaços ao todo, 2 pontos flutuantes (dos centavos).
print('-' * 39)
