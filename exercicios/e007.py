'''
Exercício 007 - Feito
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
'''

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2) / 2

# "{:.1f}" significa algo como, depois do ponto flutuante, coloque apenas 1 dígito.
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}.'.format(n1, n2, m))
