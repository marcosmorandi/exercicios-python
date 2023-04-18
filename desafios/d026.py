'''
Desafio 026 - Feito
Faça um programa que leia uma frase pelo teclado e mostre:
* Quantos vezes aparece a letra "A".
* Em que posição ela aparece a primeira vez.
* Em que posição ela aparece a última vez.
'''

frase = str(input('Digite uma frase: ')).lower().strip() # Independente de como o usuário digitar, "lower" joga tudo para minúsculo. "strip" remove os espaços antes e depois da string.
print(f'A letra "A" aparece {(frase.count("a"))} vezes na frase.') # Não tente fazer o programa inteiro de uma vez, faça por partes e vá testando.
print(f'A primeira letra "A" apareceu na posição {(frase.find("a")+1)}.') # "+1" pois para o Pyhon é posição "0", mas para pessoas faz mais sentido posição "1". Então 0 + 1.
print(f'A última letra "A" apareceu na posição {(frase.rfind("a")+1)}.') # "rfind" é para iniciar a procura pelo lado direito, do final em direção ao começo.
