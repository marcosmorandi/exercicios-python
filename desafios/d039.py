'''
Desafio 039 - Feito
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date # Importa o ano atual.
# date.today().year (ano atual).

ano_nascimento = int(input('Qual seu ano de nascimento: '))
idade = date.today().year - ano_nascimento

print(f'Quem nasceu em {ano_nascimento} tem {idade} em {date.today().year}.')

if date.today().year - ano_nascimento < 18:
    print('Ainda vai se alistar.')
    tempo = 18 - (date.today().year - ano_nascimento)
    if tempo == 1:
        print(f'Ainda falta {tempo} ano para o alistamento.')
        print(f'Seu alistamento será em {(ano_nascimento) + 18}')
    else:
        print(f'Ainda faltam {tempo} anos para o alistamento.')
        print(f'Seu alistamento será em {(ano_nascimento) + 18}')
elif date.today().year - ano_nascimento == 18:
    print('É hora de se alistar.')
elif date.today().year - ano_nascimento > 18:
    print('Já passou do tempo do alistamento.')
    tempo = (date.today().year - ano_nascimento) - 18
    if tempo == 1:
        print(f'Passou {tempo} ano do prazo de alistamento.')
        print(f'Seu alistamento foi ou deveria ter sido em {(ano_nascimento) + 18}')
    else:
        print(f'Passaram {tempo} anos do prazo de alistamento.')
        print(f'Seu alistamento foi ou deveria ter sido em {(ano_nascimento) + 18}')
