'''
Desafio 044 - Feito
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: Preço normal
- 3x ou mais no cartão: 20% de juros
'''

valor_produto = float(input('Qual o valor do produto: R$ '))
forma_pagamento = str(input('''Qual a forma de pagamento:
[ 1 ] - À vista dinheiro/cheque
[ 2 ] - À vista no cartão
[ 3 ] - Em até 2x no cartão
[ 4 ] - 3x ou mais no cartão
  '''))

if forma_pagamento == '1':
    valor_produto = valor_produto - (valor_produto * 10 / 100)
    print(f'O valor do produto com desconto de 10% fica R$ {valor_produto:.2f}')
elif forma_pagamento == '2':
    valor_produto = valor_produto - (valor_produto * 5 / 100)
    print(f'O valor do produto com desconto de 5% fica R$ {valor_produto:.2f}')
elif forma_pagamento == '3':
    print(f'O valor do produto fica R$ {valor_produto:.2f}')
elif forma_pagamento == '4':
    valor_produto = valor_produto + (valor_produto * 20 / 100)
    print(f'O valor do produto fica R$ {valor_produto:.2f}')
else:
    print('Forma de pagamento escolhida inválida. Tente de novo.')
