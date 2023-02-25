'''
Desafio 015
Escreva um programa que pergunte a quantidade de Km percorridos por um carro...
alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço...
a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por Km rodado.
'''

km_rodado = float(input('Quantos Km foram percorridos: '))
dias_alugados = float(input('Por quantos dias ele foi alugado: '))

# calculo do preço
preco_pagar = (0.15 * km_rodado) + (dias_alugados * 60)

print('{} Km percorridos e {} dias alugados.'.format(km_rodado, dias_alugados))
print('O preço total a pagar pelo aluguel é de R$ {} .'.format(preco_pagar))
