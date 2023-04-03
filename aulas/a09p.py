frase = 'Curso em Vídeo Python'
print(frase[::2]) # Do inicio ao final pulando de dois em dois.

# Forma de imprimir texto curto.
print('oi')

# Forma de imprimir texto longo com quebra de linha extamente como digitado.
print('''Welcome! Are you completely new to programing?
about why and how to get started with Python. Fortunately
an experienced programmer in any programing language
(whaterver it may be) can pick up Phython very quickly.
Its also easy for beginners to use and learn, so jump in!''')

# Sem o "pint()" vira um comentário que não é exibido.
'''Bem-vindo! Você é completamente novo em programação?
sobre por que e como começar a usar o Python. Felizmente
um programador experiente em qualquer linguagem de programação
(o que quer que seja) pode pegar Phython muito rapidamente.
Também é fácil para os iniciantes usarem e aprenderem, então entre!'''

frase = 'Curso em Vídeo Python'
print(frase.count('o')) # Contando quantas vezes tem "o".
print(len(frase)) # Vê o tamanho da frase.

# Troca a primeira frase(quando presente) pela segunda.
print(frase.replace('Python', 'Android')) # Mas não salva, para salvar: " frase = frase.replace('Python', 'Android')"

print('Curso' in frase) # Verifica se a palavra "Curso" está presente na variável "frase". Se sim retorna "True".
print(frase.find('vídeo')) # Procura a palavra "vídeo", como não existe(não em minúsculo), retorna "-1".
print(frase.split()) # Divide a frase.
dividido = frase.split() # "dividido" recebe o "frase.split()".
print(dividido[0]) # Exibe a parte "0" do split, ou seja, "Curso".
print(dividido[2][3]) # Pega o dividido 2(Vídeo) e mostra a letra 3(e).
