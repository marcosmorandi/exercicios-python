'''
Exercício 024 - Feito
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
'''

cid = str(input('Em que cidade você nasceu? ')).strip() # ".strip" remove espaços vazios antes e depois da string.
print(cid[:5].upper() == 'SANTO') # Independente de como o usuário digitar(maiúscula, minúscula, misturado), ele joga para maiúscula e verifica a palavra.
