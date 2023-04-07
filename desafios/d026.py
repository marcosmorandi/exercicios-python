'''
Desafio 026 - Não feito, ver aula.
Faça um programa que leia uma frase pelo teclado e mostre:
* Quantos vezes aparece a letra "A".
* Em que posição ela aparece a primeira vez.
* Em que posição ela aparece a última vez.
'''

frase = input(str('Digite uma frase: '))

conta1 = frase.count('A')
conta2 = frase.count('a')
aparece_vezes = conta1 + conta2 # Certo
aparece_primeiro = frase.find('a') # Errado
aparece_ultimo = frase.find('a') # Errado

print(f'''Aparece a letra "A" ou "a" {aparece_vezes} veze(s).
A primeira vez na posição {aparece_primeiro}.
A ultima vez na posição {aparece_ultimo}''')
