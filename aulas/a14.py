'''
Estrutra de repetição ou laço de repetição "while".

O "for" não serve para 100% das situações, nessas situações podemos usar o "while".
O "for" precisa de um limite, de tanto até tanto, se não souber o limite não da para o "for", precisa do "while".
"while" literalmente pode-se traduzir como "enquanto".
"for" estrutura de repetição com variável de controle.
"while" estrutura de repetição com teste lógico.
Não existe diferença de velocidade de execução entre o "for" e o "while", cada um se usa em uma situação.
O "while" serve para quando se sabe e quando não se sabe o limite.
Quando não se sabe o limite não se pode usar o "for".
'''

# for c in range(1, 10):
#     print(c)
# print('Fim')

# c = 1
# while c < 10:
#     print(c)
#     c = c + 1 # Ou "c += 1".
# print('Fim')

# n = 1
# while n != 0:
#     n = int(input('Digite um valor: '))
# print('Fim')

# r = 's'
# while r == 's':
#     n = int(input('Digite um valor: '))
#     r = str(input('Quer continuar? [S/N] ')).lower()
# print('Fim')

n = 1
par = impar = 0 # Também pode "par = 0" e "impar = 0"
while n != 0:
    n = int(input('Digite um valor, para para digite "0": '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Fim\nVoce digitou {par} números pares e {impar} números ímpares!')
