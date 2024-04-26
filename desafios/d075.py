'''
Exercício 075 - Feito
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''

valores = (int(input('Digite o 1º valor: ')), int(input('Digite o 2º valor: ')), 
           int(input('Digite o 3º valor: ')), int(input('Digite o 4º valor: ')))
print(f'Você digitou os valores {valores}.')
print(f'O número 9 apareceu {valores.count(9)} veze(s).') # "{num.count(9)}" contando quantas vezes apareceu o valor "9" dentro da tupla.
if 3 in valores: # Se apareceu o 3.
    print(f'O valor 3 apareceu na {valores.index(3)+1}ª posição.') # "{num.index(3)+1}" qual o indice do valor 3. Onde aparece pela primeira vez.
else: # Se não apareceu o 3.
    print('O valor 3 não apareceu nunhuma vez.')
print('Os valores pares digitados foram: ', end='') # "if" "else" não funciona na verificação de pares.
for n in valores:
    if n % 2 == 0:
        print(n, end= ' ')
