'''
Desafio 015 - Feito
Escreva um programa que pergunte a quantidade de Km percorridos por um carro...
alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço...
a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por Km rodado.
'''

dias_alugados = float(input('Quantos dias o carro foi alugado: '))
km_rodado = float(input('Quantos Km foram percorridos: '))

# calculo do preço
preco_pagar = (dias_alugados * 60) + (0.15 * km_rodado)

print('{:.0f} dias alugados e {:.0f} Km percorridos.'.format(dias_alugados, km_rodado))
print('O preço total a pagar pelo aluguel do carro é de R$ {:.2f}'.format(preco_pagar))
