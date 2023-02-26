'''
Exercício 14 - Feito
Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
'''

c = float(input('Informe a temperatura em °C: '))

# Espaço entre os operadores deixa o código mais legível.
# Pela regra de precedência, os parênteses nesse caso são opcionais. Gosto da legibilidade que eles dão.
f = ((9 * c) / 5 ) + 32 
print('A temperatura de {}°C corresponde a {}°F'.format(c, f))
