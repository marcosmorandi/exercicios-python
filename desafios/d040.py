'''
Desafio 040 - Feito
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando um mensagem no
final, de acordo com a média atingida:
- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: Recuperação
- Média de 7.0 ou superior: Aprovado
'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print(f'Media {media:.1f}\nReprovado.')
elif media == 5 or media <= 6.9:
    print(f'Media {media:.1f}\nRecuperação.')
elif media >= 7:
    print(f'Media {media:.1f}\nAprovado.')
