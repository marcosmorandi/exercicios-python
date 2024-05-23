'''
Exercício 072 - Feito
Crie um programa que tem uma tupla totalmente preenchida com uma contagem por extenso,
do zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso.
Se colocar um numero menor que 0 ou maior que 20 tem que mostrar uma mensagem para digitar novamente.
'''

contagem = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
            'doze', 'treze', 'quatorze', 'quize', 'dezesseis', 'dezesste', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {contagem[num]}')
