'''
Desafio 037 - Feito
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
    print(f'''Conversão para binário!
{numero} convertido para binário é {bin(numero)[2:]}.''') # O Python tem um conversor interno de decimal para binario, octal e hexadecimal.
elif base_conversao == 2:
    print(f'''Conversão para octal!
{numero} convertido para octal é {oct(numero)[2:]}''') # "[2:]" técnica de fatiamento de string, a posição 0 e 1 não quero que apareça, mostra da 3ª posição ao final.
elif base_conversao == 3:
    print(f'''Conversão para hexadecimal!
{numero} convertido para hexadecimal é {hex(numero)[2:]}''') # Sem o fatiamento ele imprime dois caracteres referente ao tipo de conversão.
else:
    print('Opção inválida!')
