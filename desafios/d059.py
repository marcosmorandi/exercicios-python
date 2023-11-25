'''
Desafio 059 - Feito
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
operacao = 0
while operacao != 5:
    print('-' * 50) # Muito melhor do que digitar 50 vezes o caracter "-".
    operacao = int(input('Escolha a operação:\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\nSua escolha: '))
    print('-' * 50)

    if operacao == 1:
        soma = n1 + n2
        print(f'O resultado da soma de {n1} + {n2} é {soma}.')

    elif operacao == 2:
        multiplicacao = n1 * n2
        print(f'O resultado da multiplicação de {n1} X {n2} é {multiplicacao}.')

    elif operacao == 3:
        if n1 > n2:
            print(f'O primeiro valor ({n1}) é o maior.')
        elif n2 > n1:
            print(f'O segundo valor ({n2}) é o maior.')
        else:
            print('Ambos valores são iguais')

    elif operacao == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))

    elif operacao == 5:
        print('Você escolheu sair!')

    else:
        print('Opção inválida, tente novamente!')

print('Fim do programa.')
