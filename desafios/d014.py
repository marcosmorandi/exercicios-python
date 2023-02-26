'''
Desafio 014 - Feito
Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
'''

temperatura_celcius = float(input('Digite a temperatura em Graus Celsius °C: '))
temperatura_fahrenheit = (temperatura_celcius * 9 / 5) + 32
print('A temperatura em Graus Celsius {:.0f}°C convertida em Graus Fahrenheit fica {:.1f}°F'.format(temperatura_celcius, temperatura_fahrenheit))
