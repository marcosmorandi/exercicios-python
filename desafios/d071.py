'''
Desafio 071
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usupario 
qual será o valor sacado (número inteiro) e o programa vai informar quantas células de cada valor 
serão entregues.
OBS: Considere que o caixa possui células de R$ 50, R$ 20, R$ 10 e R$ 1.
'''

# Exemplo:
# ========================
#        Banco CEV        
# ========================
# Que valor você quer sacar: RS 1234
# Total de 24 cédula(s) de R$ 50
# Total de 1 cédula(s) de R$ 20
# Total de 1 cédula(s) de R$ 10
# Total de 4 cédula(s) de R$ 1
# ========================
# Volte sempre ao Banco CEV! Tenha um bom dia!

print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
