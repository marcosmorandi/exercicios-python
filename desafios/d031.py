'''
Desafio 031 - Feito
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$ 0,50 por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas.
'''

distancia_viagem = float(input('Qual a distância da viagem em Km: '))
if distancia_viagem <= 200:
    valor = distancia_viagem * 0.50
    print(f'O valor da passagem ficou em R$ {valor:.2f}.')
else:
    valor = distancia_viagem * 0.45
    print(f'O valor da passagem ficou em R$ {valor:.2f}.')
