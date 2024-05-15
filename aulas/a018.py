# Variáves Compostas (Listas) Parte 2
'''
dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])

pessoas = list()
pessoas.append(dados[:]) # "[:]" Faz uma cópia.
pessoas = [['pedro',25],['maria',19],['joao'32]]
print(pessoas[0][0]) # Pessoa 0, item 0, "pedro".
print(pessoas[1]) # Todo conteudo do pessoas 1, "Maria, 19".
'''

'''
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
'''

'''
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[2][1]) # "galera[2][1]" mostra galera 2 (joaquim, 13), item 1 (13).
for p in galera:
    print(p)
    print(p[0])
    print(p[1])
    print(f'{p[0]} tem {p[1]} anos de idade.')
'''

galera = list()
dado = list() # "galera = dado = list()" não pode fazer, não funciona.
totmai = totmen = 0 # Isso pode fazer com variáveis simples, mas não com compostas.

for contador in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maior(es) e {totmen} menor(es) de idade.')
