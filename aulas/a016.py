# Variáveis Compostas (Tuplas)

# tuplas são imutáveis
# lanche = () [] {}; tupla(), lista[], dicionário{}

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

print(lanche[0])

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi pra caramba!')

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

for cont in range(0, len(lanche)): # Mostrando a posição da variável.
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')

for pos, comida in enumerate(lanche): # Mostrando a posição da variável.
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')

print(sorted(lanche)) # Coloca em ordem em alfabética.
print(lanche)

pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa) # Apaga a viriável.
print(pessoa)
