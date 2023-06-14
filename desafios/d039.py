'''
Desafio 039 - Quase pronto
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date # Importa o ano atual.
# date.today().year (ano atual).

ano_nascimento = int(input('Qual seu ano de nascimento: '))

if date.today().year - ano_nascimento < 18:
    print('Ainda vai se alistar.')
elif date.today().year - ano_nascimento == 18:
    print('É hora de se alistar.')
elif date.today().year - ano_nascimento > 18:
    print('Já passou do tempo do alistamento.')
