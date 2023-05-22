'''
Exercício 031 - Feito
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$ 0,50 por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas.
'''

# Forma Normal:
distancia = float(input('(FN)Qual é a distância da sua viagem? '))
print(f'(FN)Você está prestes a começar uma viagem de {distancia}Km.')
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'(FN)E o preço da sua passagem será de R$ {preco:.2f}.')

# If in Line, Operador Ternario ou If Simplificado:
distancia = float(input('(IS)Qual é a distância da sua viagem? '))
print(f'(IS)Você está prestes a começar uma viagem de {distancia}Km.')
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'(IS)E o preço da sua passagem será de R$ {preco:.2f}.')
