'''
Desafio 053 - !Bug! Da segunda frase em diante ele não reconhece como palíndromo.
Crie um programa que leia uma frase qualquer e diga se ela é palíndromo, desconsidere os espaços.
Palíndromo: Frase que pode ser lida do inicio ao fim ou do fim ao inicio e fica igual, desconsiderando espaços.
Ex: apos a sopa, a sacada da casa, o lobo ama o bolo, anotaram a data da maratona.
'''

def palindromo(frase):

    # Remove espaços e converte a frase para letras minúsculas.
    frase = frase.replace(" ", "").lower()

    # Verifica se a frase é igual a sua inversa.
    return frase == frase[::-1]

# Solicita ao usuário que digite uma frase.
frase = str(input('Digite uma frase para verificar se é palíndromo: '))

# Inicializa uma variável para armazenar a resposta.
palindromo = True

# Itera sobre a metade da frase (desconsiderando os espaços)
for c in range(len(frase) // 2):
    if frase[c] != frase[-c - 1]:
        palindromo = False
        break

# Verifica se a frase é um palídromo
if palindromo:
    print(f'A frase {frase} é um palíndromo.')
else:
    print(f'A frase {frase} não é um palíndromo')
