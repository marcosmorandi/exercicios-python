'''
Desafio 072 - Feito
Crie um programa que tem uma tupla totalmente preenchida com uma contagem por extenso,
do zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso.
Se colocar um numero menor que 0 ou maior que 20 tem que mostrar uma mensagem para digitar novamente.
'''

contagem = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
             'onze', 'doze', 'treze', 'quatorze', 'quize', 'dezesseis', 'dezesste', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if numero >= 0 and numero <= 20: # Se igual ou maior a 0 e menor ou igual a 20 para a repetição e mostra o número.
        break
    print('Numero inválido! Tente novamente. ', end='') # Se não imprime o erro e fica pedindo o número.
print(f'Você digitou o número {contagem[numero]}') # Procura a posição do número digitado na contagem.
