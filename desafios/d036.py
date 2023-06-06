'''
Desafio 036
Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o
empréstimo será negado. Desconsidere os juros.
'''

valor_casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário do comprador? '))
anos_pagando = int(input('Em quantos anos vai pagar? '))
