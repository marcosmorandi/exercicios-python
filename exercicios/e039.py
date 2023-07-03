'''
Exercício 039 - Feito
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date
atual = date.today().year
nascimento = int(input('Qual foi o ano de nascimento: '))
idade = atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} em {atual}')
if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento.')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}.')
elif idade > 18: # Poderia ser um "else", mas o "elif" ajuda na compreensão do código.
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}.')
