'''
Desafio 056 - !Corrigir!
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
    media_idade += idade
    if sexo == "m" or sexo == "M":
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    else:
        if sexo == "m" or sexo == "M" and idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            nome_homem_mais_velho == nome
    if sexo == "f" or sexo == "F" and idade < 20:
        mulheres_menos_vinte_anos += 1
media_idade = media_idade / 4
print(f'\nA média de idade do grupo é de {media_idade} anos.')
print(f'O homem mais velho tem {idade_homem_mais_velho} anos e se chama {nome_homem_mais_velho}.')
print(f'Ao todo são {mulheres_menos_vinte_anos} mulheres com menos de 20 anos.')
