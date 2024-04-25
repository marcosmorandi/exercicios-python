# Variáves Compostas (Listas)

# Tupla, com "()", imutável.
# num = (2, 5, 9, 1)
# print(num)

# Lista, com "[]", mutável.
# num = [2, 5, 9, 1]
# print(num)
# num[2] = 3 # Muda o valor na posição 2 para 3.
# num.append(7) # Adiciona o valor 7 ao final da lista.
# num.insert(2, 0) # Na posição 2 insere o valor 0.
# num.pop(2) # Remove o valor na posição "2". Caso fique "()" remove o último valor.
# num.insert(2, 2) # Na posição 2 insere o valor 2.
# if 4 in num:
#     num.remove(4) # Se tiver, remove o número 4...
# else:
#     print('Não achei o número 4.') # ... se não, avisa que não achou.
# num.remove(2) # Remove o elemnto da posição 2.
# print(num)
# num.sort() # Coloca em ordem crescente.
# print(num)
# num.sort(reverse=True) # Coloca em ordem decrescente.
# print(num)
# print(f'Essa lista tem {len(num)} elementos.') # Mostra quantos elementos tem a lista.

# Iniciando Lista vazia.
# valores = [] # Lista também pode ser iniciado com "valores = list()".
# valores.append(5)
# valores.append(9)
# valores.append(4)
# print(valores)
# for v in valores:
#     print(f'{v}...')
# for c, v, in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}!')
# print('Cheguei ao final da lista.')

# valores = list()
# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))
# for c, v, in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}!')

a = [2, 3, 4, 7]
b = a[:] # "[:]" "B" recebe todos os itens de "A". Não cria uma ligação, mas uma cópia.
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
