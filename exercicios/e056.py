'''
Exercício 056 - Feito
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
* A média de idade do grupo.
* Qual é o nome do homem mais velho.
* Quantas mulheres têm menos de 20 anos.
'''

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade # Nesse caso a "somaidade" recebe ela mesma mais a "idade".
    if p == 1 and sexo in 'Mm': # Nesse caso o "in" compara "M" e "m", maiúsculo e minusculo.
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1 # "totmulher20" recebe ele mesmo mais 1.
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
print(f'Ao todo são {totmulher20} mulher(es) com menos de 20 anos.')
