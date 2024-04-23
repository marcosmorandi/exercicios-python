'''
Desafio 073 - Feito
Crie um tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileio de Futebol,
na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense(Flamengo).
'''

tabela = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 
          'Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza', 
          'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco da Gama', 
          'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG') # Ano 2023.
print(f'Os 5 primeiros colocados são {tabela[0:5]}.') # "{tabela[0:5]}" exibe da primeira posição (0) até a anterior a sexta (5) posição, que é a 4 sem exibir a sexta 5.
print(f'Os 4 últimos colocados da tabela são {tabela[-4:]}.') # "{tabela[-4:]}" exibe do quarto último até o final da lista.
print(f'Os times em ordem alfabética são {sorted(tabela)}.') # "{sorted(tabela)}" mostra a variavel times em ordem alfabética.
print(f'O time do Flamengo está na {tabela.index("Flamengo")+1}ª posição.') # "{times.index("Flamengo")+1}" procura a string Flamengo no index e exibe a posição + 1, pois a posição original conta 0.
