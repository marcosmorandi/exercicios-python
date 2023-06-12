'''
Exercício 037 - Feito
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
'''

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}.') # O Python tem um conversor interno de decimal para binario, octal e hexadecimal.
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}.') # "[2:]" técnica de fatiamento de string, a posição 0 e 1 não quero que apareça, mostra da 3ª posição ao final.
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}.') # Sem o fatiamento ele imprime dois caracteres referente ao tipo de conversão. 
else:
    print('Opção inválida! Tente novamente.')
