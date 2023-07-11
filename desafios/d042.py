'''
Desafio 042 - Feito
Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
será formado:
- Equilátero: Todos os lado iguais
- Isósceles: Dois lados iguas
- Escaleno: Todos os lados diferentes
'''

reta_1 = float(input('Digite o tamanho da primeira reta: '))
reta_2 = float(input('Digite o tamanho da segunda reta: '))
reta_3 = float(input('Digite o tamanho da terceira reta: '))

if ((reta_1 + reta_2) > reta_3) and ((reta_1 + reta_3) > reta_2) and ((reta_2 + reta_3) > reta_1):
    print('Essas medidas podem formar um triângulo.')
    if reta_1 == reta_2 and reta_2 == reta_3 and reta_1 == reta_3:
        print('Essas medidas formam um triângulo equilátero, com todos lados iguais.')
    elif reta_1 != reta_2 and reta_2 != reta_3 and reta_1 != reta_3:
        print('Essas medidas formam um triângulo escaleno, com todos os lados diferentes.')
    else:
        print('Essas medidas formam um triângulo isósceles, com dois lados iguais.')
else:
    print('Essas medidas não podem formar um triângulo.')
