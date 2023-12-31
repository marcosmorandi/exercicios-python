'''
Desafio 067 - Feito
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
'''

# Exemplo:
# ---------------------------------
# Quer ver a tabua de que valor: x
# ---------------------------------
# (mostra tabuada)
# ---------------------------------
# Quer ver a tabua de que valor: -x
# ---------------------------------
# Programa tabuada encerrado. Volte sempre!

while True:
    tabuada = int(input('Quer ver a tabuada de qual valor(-qualquer número para parar): '))
    if tabuada < 0:
        break
    for controle in range(1, 11):
        print(f'{controle} x {tabuada} = {controle * tabuada}')
print('Programa tabuada encerrado. Volte sempre!')
