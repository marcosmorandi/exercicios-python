'''
Desafio 038 - Feito
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro número é maior.
- O segundo número é maior.
- Não existe valor maior, os dois são iguais.
'''

primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))

if primeiro_numero > segundo_numero:
    print(f'O primeiro número ({primeiro_numero}) é maior que o segundo ({segundo_numero}).')
elif segundo_numero > primeiro_numero:
    print(f'O segundo número ({segundo_numero}) é maior que o primeiro ({primeiro_numero}).')
else:
    print(f'Não existe valor maior, os números são iguais ({primeiro_numero} e {segundo_numero}).')
