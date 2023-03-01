'''
Desafio 018 - Feito
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno...
e tangente desse ângulo.
'''

# Importando toda a biblioteca "math".
import math

# Ler o ângulo em graus.
angulo = float(input('Digite o ângulo em graus: '))

# Converter o ângulo de graus para radianos.
angulo_para_radianos = math.radians(angulo)

# Calcular o seno, cosseno e tangente do ângulo em radianos.
seno = math.sin(angulo_para_radianos)
cosseno = math.cos(angulo_para_radianos)
tangente = math.tan(angulo_para_radianos)

# Exibir os resultados na tela.
print(f'O seno de {angulo} graus é {seno:.2f}')
print(f'O cosseno de {angulo} graus é {cosseno:.2f}')
print(f'A tangente de {angulo} graus é {tangente:.2f}')
