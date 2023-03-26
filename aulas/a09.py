# Aula 09 - Manipulando Cadeias de Texto

frase = 'Curso em Video Python' # Atribuição de uma string dentro de uma variável.
# [C][u][r][s][o][ ][e][m][ ][V][i][d][e][o][ ][P][y][t][h][o][n] índice de 0 a 20.
# 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20

# Fatiamento
frase [9] # V, o 9.
frase [9:13] # Vai do 9 ao 12, pois o 13 não é exibido.
frase [9:21:2] # Vai do 9 ao 20, exibindo e pulando 1(2 não é exibido).
frase [:5] # Vai do começo(0) até 4.
frase [15:] # Vai do 15 até o final.
frase [9::3] # Começa no 9 e vai até o final, exibindo e pulando 2(3 não é exibido).

# Análise
len(frase) # 21 caracteres.
frase.count('o') # Conta os 'o'(minúsculos) na frase, no caso "3".
frase.count('o',0,13) # Conta os 'o' do 0 ao 12(lembre-se que o ultimo valor é sempre ignorado), no caso "1".
frase.find('deo') # Mostra onde começa(se tiver) o "deo", nesse caso no 11.
frase.find('Android') # Retorna "-1", o que significa que a string não foi encontrada, não existe.
'Curso' in frase # "True" pois existe a string "Curso" na variável "frase".

# Transformação
frase.replace('Python', 'Android') # Onde tem "Python" ele substitue por "Android".
frase.upper() # Deixa tudo em maiúsculas, mantendo inalterada o que já estava em maiúsculas.
frase.lower() # Deixa tudo em minúsculas.
frase.capitalize() # Deixa só o primeiro caractere em maiúscula e o restante em minúscula.
frase.title() # No começo e depois de qualquer espaço, ele deixa em maiúscula.
frase.strip() # Remove espaços inuteis no inicio e fim da string.
frase.rstrip() # Remove espaços do lado direito, right, da string.
frase.lstrip() # Remove espaços do lado esquerdo, left, da string.

# Divisão
frase.split() # Divide onde tem espaço. Cada palavra recebe indexação nova.

# Junção
'-'.join(frase) # Cria um string única e onde tem espaço junta com o "-", se quiser juntar com espaço em branco "' '-.join(frase)".

#29m
