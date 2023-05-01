'''
Desafio 029 - Feito
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada Km acima do limite.
'''

velocidade = int(input('Qual a velocidade do carro: ')) # Lê a velocidade do carro.

if velocidade <= 80: # Se a velocidade for menor ou igual a 80:
    print(f'Velocidade {velocidade}Km/h, limite 80km/h, dentro do limite!')
else: # Senão:
    print(f'Velocidade {velocidade}Km/h, limite 80km/h, fora do limite, multado!')
    multa = float(velocidade - 80) * 7 # Calcula R$ 7,00 por cada Km/h acima do limite.
    print(f'Valor da multa: R$ {multa:.2f}') # Exibe a multa.
