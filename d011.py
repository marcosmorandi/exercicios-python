'''
Desafio 011 - em desenvolvimento
Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pinta-lá...
...sabendo que cada litro de tinta, pinta uma área de 2m².
'''

largura = float(input('Qual a largura da parede em metros? '))
altura = float(input('Qual a altura da parede em metros? '))

area = largura * altura
tinta = 0 # errado, arrumar

print('A área da parede é de {} metros, será necessário {} litro(s) de tinta para pintar.'.format(area, tinta))
