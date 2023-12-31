'''
Exercício 066 - Feito
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''

soma = cont = 0 # Não precisa inicializar a variável "num".
while True: # Transforma em loop infinito, pois o enquanto não fica "False" automaticamente. Para parar usar a condição de parada.
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}!')
