'''
Desafio 037 - Feito? Não!
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
'''

numero = int(input('Digite um número inteiro: '))
base_conversao = int(input('''
                            Escolha a base de conversão
                            1 - Binário
                            2 - Octal
                            3 - Hexadecimal
                            
                            '''))

if base_conversao == 1:
    print('Conversão para binário!')
elif base_conversao == 2:
    print('Conversão para octal!')
elif base_conversao == 3:
    print('Conversão para hexadecimal!')
else:
    print('Opção inválida!')
