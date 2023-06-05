# Condições Aninhadas

# Dentro de um "if" pode usar quantos "elif" quiser, "else" usa-se uma ou nenhuma vez.

nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome comum!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino.')
else:
    print('Sorte sua não se chamar Gustavo.')
print(f'Tenha um bom dia {nome}.')
