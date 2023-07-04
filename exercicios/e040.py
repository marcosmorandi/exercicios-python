'''
Exercício 040 - Feito
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando um mensagem no
final, de acordo com a média atingida:
- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: Recuperação
- Média de 7.0 ou superior: Aprovado
'''

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1:.1f} e {nota2:.1f} a média do aluno é {media:.1f}')
if 7 > media >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif media < 5:
    print('O aluno está REPROVADO.')
elif media >= 7:
    print('O aluno está APROVADO.')
