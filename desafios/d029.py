'''
Desafio 029
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada Km acima do limite.
'''

velocidade = int(input('Qual a velocidade do carro: '))

if velocidade <= 80:
    print(f'Velocidade {velocidade}Km/h, limite 80km/h, dentro do limite!')
else:
    print(f'Velocidade {velocidade}Km/h, limite 80km/h, fora do limite, multado!')
