'''
Desafio 056 - Feito
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
* A média de idade do grupo.
* Qual é o nome do homem mais velho.
* Quantas mulheres têm menos de 20 anos.
'''

soma_idade = 0
media_idade = 0
nome_homem_mais_velho = ''
idade_homem_mais_velho = 0
mulheres_menos_vinte_anos = 0
for pessoa in range(1, 5):
    print(f'\n----- {pessoa}ª Pessoa -----')
    nome = str(input(f'Qual o nome da {pessoa}ª pessoa: '))
    idade = int(input(f'Qual a idade da {pessoa}ª pessoa: '))
    sexo = str(input(f'Qual o sexo da {pessoa}ª pessoa (M/F): '))
    soma_idade += idade # Nesse caso a "soma_idade" recebe ela mesma mais a "idade".
    if pessoa == 1 and sexo in 'Mm': # Nesse caso o "in" compara "M" e "m", maiúsculo e minúsculo.
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    elif sexo in 'Mm' and idade > idade_homem_mais_velho:
        nome_homem_mais_velho = nome
        idade_homem_mais_velho = idade
    elif sexo in 'Ff' and idade < 20:
        mulheres_menos_vinte_anos += 1 # Aqui "mulheres_menos_vinte_anos" recebe ele mesmo mais 1.
media_idade = soma_idade / 4
print(f'A média da idade do grupe é de {media_idade} anos.')
print(f'O homem mais velho do grupo é o {nome_homem_mais_velho}, com {idade_homem_mais_velho} anos.')
print(f'No total {mulheres_menos_vinte_anos} mulheres tem menos de 20 anos.')
