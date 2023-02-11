'''
Desafio 008 - Feito
Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
'''

metros = float(input('\nDigite uma valor em metros (use "." ao invés de ","): '))

centimetros = metros * 100
milimetros = metros * 1000

print('\n{} m (metros) convertido é: \nEm centimetros {:.0f} cm. \nEm milimetros {:.0f} mm.\n'.format(metros, centimetros, milimetros))
