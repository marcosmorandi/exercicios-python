'''
Desafio 069 - Feito
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
'''

# Exemplo:
# ---------------------
#  Cadastre Uma Pessoa
# ---------------------
# Idade: 33
# Sexo [M/F]: M
# -------------------
# Quer continar [S/N]: S
# ---------------------
#  Cadastre Uma Pessoa
# ---------------------
# Idade: 25
# Sexo [M/F]: g
# Sexo [M/F]: y
# Sexo [M/F]: f
# -------------------
# Quer continar [S/N]: w
# Quer continar [S/N]: s
# ---------------------
#  Cadastre Uma Pessoa
# ---------------------
# Idade: 8
# Sexo [M/F]: m
# ---------------------
# Quer continar [S/N]: n
# ========== Fim do Programa ==========
# Total de pessoas com mais de 18 anos: 2
# Ao todo temos 2 homens cadastrados
# E temos 1 mulher(es) com menos de 20 anos

mais_18 = homens = mulheres_menos_20 = 0
while True:
    print('-'*20)
    print('Cadastre uma pessoa')
    print('-'*20)
    idade = int(input('Idade: '))
    if idade > 18:
        mais_18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
    print('-'*20)
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if continua == 'N':
        break
print('='*10 + ' Fim do programa ' + '='*10)
print(f'Total de pessoas com mais de 18 anos: {mais_18}\nAo todo temos {homens} homem(ns) cadastrados\nE temos {mulheres_menos_20} mulher(es) com menos de 20 anos.')
