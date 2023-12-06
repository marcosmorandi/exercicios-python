'''
Exercício 062 - Feito
Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
'''


# Desafio 061 - Feito
# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
# da progressão usando a estrutura "while".

# print('-=-' * 10)
# print('Gerador de PA')
# print('-=-' * 10)

# primeiro = int(input('Primeiro termo: '))
# razao = int(input('Razão da PA: '))
# termo = primeiro
# contador = 1
# print('Os 10 primeiros termos dessa PA são:')
# while contador <= 10:
#     print(f'{termo} -> ', end='')
#     termo += razao
#     contador += 1
# print('FIM')

print('-=-' * 10)
print('Gerador de PA')
print('-=-' * 10)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
