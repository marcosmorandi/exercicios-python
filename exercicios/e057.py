'''
Exercício 057 - Feito
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

sexo = str(input('Infome o seu sexo [M/F]: ')).strip().upper()[0] # "strip" elimina possíveis espaços vazios, "upper" deixa tudo maiúscula, "[0]" pega só a primeira letra.
while sexo not in 'MmFf': # "enquanto não for...", com o "upper" nem precisaria testar as minúsculas, mas assim deixa o código mais legível.
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
