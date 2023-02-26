'''
Exercício 011 - Feito
Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pinta-lá...
...sabendo que cada litro de tinta, pinta uma área de 2m².
'''

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura

print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².'.format(largura, altura, area))
tinta = area / 2

print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
