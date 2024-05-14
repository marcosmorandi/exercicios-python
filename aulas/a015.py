''' Interropendo repetições "while" e as "fstrings". '''

# Loop infinito:

# cont = 1
# while True:
#     print(cont, '-> ', end='')
#     cont += 1
# print('Acabou')

n = s = 0 # No Python se inicializa variavél, não se declara.
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break # Comando "break" para o laço, dispensando o uso da flag.
    s += n
print(f'A soma vale {s}')
# O "f" antes das aspas, se chama "fstrings", atualização do Python 3.6.3, para simplificar o "print".
# Se chama PEP 498, Python Enhancement Proposal (Proposta de Melhoria do Python).
# Com o "f" ele começa a usar um técnica chamada de interpolação dentro de strigs.


# Exemplos de "prints" antigos e com as atuais "fstrings", qualquer forma funciona:
nome = 'Jose'
idade = 33
print(f'O {nome} tem {idade} anos.') # Python 3.6+
print('O {} tem {} anos.'.format(nome, idade)) # Python 3
print('O %s tem %d anos.' % (nome, idade)) # Python 2
