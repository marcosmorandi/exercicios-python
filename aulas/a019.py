# Variáveis Compostas (Dicionários)

# Parte Teórica
'''
Tuplas () # Identifcados por parêntese.
Listas = [] ou Listas = list() # Identificadas por colchetes.
Dicionarios = {} ou Dicionarios = dict() # Identificados por chaves.

dados = {'nome':'Pedro':'idade':25} # "Pedro" deixa de ter indice "0" para ter indice "nome" e "25" deixa de ter indice "1" para ter indice "idade".
print(dados['nome']) Pedro # "dados" é o nome da estrutura e "Pedro" é o valor armazenado em "nome".
print(dados['idade']) 25

dados['sexo'] = 'M' # Cria o elemento "sexo" com o valor "M".
del dados['idade'] # Elimina o elemento "idade".

filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'Geroge Lucas'}

filme
|'Star Wars' | 1977 | 'George Lucas'|
|   titulo   | ano  |    diretor    |

print(filme.values()) # Pega a parte de cima, "star wars", etc.
print(filme.keys()) # Pega a parte de baixo, "titulo", etc.
print(filme.items()) # Pega os dois.

for k, v in filme.itens():
    print(f'O {k} é {v}') # Escreve na tela "O titulo é Star Wars"
                          #                 "O ano é 1977"
                          #                 "O diretor é George Lucas"
'''

# Parte Prática
'''
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('-' * 30)
for key in pessoas.keys():
    print(key)
print('-' * 30)
for key in pessoas.values():
    print(key)
print('-' * 30)
for key, valor in pessoas.items():
    print(f'{key} = {valor}')
print('-' * 30)
del pessoas['sexo'] # Apagando item.
for key, valor in pessoas.items():
    print(f'{key} = {valor}')
print('-' * 30)
pessoas['nome'] = 'Leandro' # Alterando item.
for key, valor in pessoas.items():
    print(f'{key} = {valor}')
print('-' * 30)
pessoas['peso'] = 98.5 # Adicionando item.
for key, valor in pessoas.items():
    print(f'{key} = {valor}')
'''

# Criando um dicinário dentro de uma lista
'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
'''

estado = dict()
brasil = list()
for contador in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # no Dicionário existe um método interno para cópia, o metodo "copy".
for estado in brasil:
    for chave, valor, in estado.items():
        print(f'O campo {chave} tem valor {valor}.')
print('-' * 30)
for estado in brasil:
    for valor in estado.values():
        print(valor, end=' ')
    print()
