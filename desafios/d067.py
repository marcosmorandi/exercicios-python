'''
Desafio 067
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

contador = 0
while True:
    tabuada = int(print('Quer ver a tabuada de qual valor(- para parar): '))
    if tabuada == -:
        break
    else:
        contador +=1
        print(f'{contador} x {tabuada} = {contador * tabuada}')
print('Programa tabuada encerrado. Volte sempre!')
