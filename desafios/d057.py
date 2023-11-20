'''
Desafio 057 - Feito
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

nome = str(input('Digite o nome: '))
sexo = str(input('Digite o sexo (M/F): ')).upper()[0].strip() # "upper" para maiúscula, "[0]" pega só a primeira letra, "strip" elimina possíveis espaços vazios.
while sexo != 'M' and sexo != 'F':
    print('Valor informado para o "sexo" inválido, tente novamente!')
    sexo = str(input('Digite o sexo (M/F): ')).upper()
if sexo == 'M':
    print(f'Nome: {nome}\nSexo: Masculino')
if sexo == 'F':
    print(f'Nome: {nome}\nSexo: Feminino')
