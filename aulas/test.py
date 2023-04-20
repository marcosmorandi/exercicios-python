nome  = str(input('Digite um nome: ')).strip()
print(f'A última posição do nome é {(len(nome))}.')
print(f'E é a letra {(nome[len(nome)])}.') # !!! IndexError: string index out of range !!! Não tem letra na posição 3.
