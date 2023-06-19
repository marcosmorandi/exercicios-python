'''
Desafio 041 - Feito
A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: Mirin
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 20 anos: Sênior
- Acima: Master
'''

from datetime import date

print(f'Ano atual: {date.today().year}')
ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))

idade = date.today().year - ano_nascimento

if idade <= 9:
    if idade == 1:
        print(f'{idade} ano')
        print('Categoria Mirin')
    else:
        print(f'{idade} anos')
        print('Categoria Mirin')
elif idade <= 14:
    print(f'{idade} anos')
    print('Categoria Infantil')
elif idade <= 19:
    print(f'{idade} anos')
    print('Categoria Junior')
elif idade <= 20:
    print(f'{idade} anos')
    print('Categoria Sênior')
else:
    print(f'{idade} anos')
    print('Categoria Master')
