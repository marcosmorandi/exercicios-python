'''
Desafio 062 - Feito
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
print(' V 3.0 ')
print('-=-' * 10)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 1
print('Os 10 primeiros termos dessa PA são:')
while contador <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    contador += 1

novo_contador = 1
mais_termos = int(input('\nSe deseja mostrar mais termos, digite o valor ou digite "0" para parar: '))
if mais_termos != 0:
    while novo_contador <= mais_termos:
        print(f'{termo} -> ', end='')
        termo += razao
        novo_contador += 1

print('FIM')
