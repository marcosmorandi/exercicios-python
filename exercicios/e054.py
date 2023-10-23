'''
Exercício 054 - Feito
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores.
'''

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input(f'Em que ano a {pess}ª pessoa nasceu: '))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoa(s) maior(es) de idade.')
print(f'E também {totmenor} pessoa(s) menor(es) de idade.')
