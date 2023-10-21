'''
Desafio 053
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando
os espaços.
Ex: "apos a sopa", "a sacada da casa", "o lobo ama o bolo", "anotaram a data da maratona".
'''

frase = str(input('Digite uma frase: ')).strip().upper() # ".strip()" tira espaços, ".upper()" deixa em maiusculo. Para realizar a comparação.
palavras = frase.split() # ".split()" separa a frase em palavras onte tem espaço.
junto = ''.join(palavras) # "''.join()" juntas as palavras sem espaços.
inverso = ''
#inverso = junto[::-1] # Simplificando 1 linha acima e 2 linhas abaixo "[::-1]", do inicio ":", ao fim ":", de trás para frente "-1". Sem o "for". Fatiamento no Python.
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de "{junto}" é "{inverso}".')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
