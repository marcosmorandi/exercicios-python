'''
Exercício 026 - Feito
Faça um programa que leia uma frase pelo teclado e mostre:
* Quantos vezes aparece a letra "A".
* Em que posição ela aparece a primeira vez.
* Em que posição ela aparece a última vez.
'''

frase = str(input('Digite uma frase: ')).lower().strip() # Pode usar o "lower" e "strip" simultaneamente.
print(f'A letra "A" aparece {(frase.count("a"))} vezes na frase.')
print(f'A primeira letra "A" aparece na posição {(frase.find("a")+1)}.')
print(f'A última letra "A" aparece na posição {(frase.rfind("a")+1)}.')
