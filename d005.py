'''
Desafio 005 - Feito
Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.
'''
numero = int(input('Digite um número: '))
numero_sucessor = numero + 1
numero_antecessor = numero - 1

print('O número digitado é {}, seu sucessor é {} e seu antecessor é {}.'.format(numero, numero_sucessor, numero_antecessor))
