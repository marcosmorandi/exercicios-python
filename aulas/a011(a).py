# Cores no Terminal

'''
Cores ANSI escape sequence
\033[0;33;44m
\033[(estilo);(cor do texto);(cor do fundo)m
"\033[" abre, "m" fecha.
Não tem necessidade de definir os 3 parâmetros, se tiver mais de um separe com ";"
Não esqueça de fechar com "\033[m" para não colorir informações posteriores.

Estilos:
0 - Nenhum
1 - Negrito
4 - Sublinhado
7 - Negativo, inverte texto e fundo.

Cor do Texto:
30 - Branco (Cinza no VSCode, padrão é o Branco)
31 - Vermelho
32 - Verde
33 - Amarelo
34 - Azul
35 - Roxo
36 - Ciano
37 - Cinza (Branco no VSCode, padrão é o Branco)

Cor do Fundo:
40 - Branco (Cinza no VSCode, padrão é o Cinza)
41 - Vermelho
42 - Verde
43 - Amarelo
44 - Azul
45 - Roxo
46 - Ciano
47 - Cinza (Branco no VSCode, padrão é o Cinza)
'''

print('\033[7;33;44mHello, World!\033[m')

a = 3
b = 5
print(f'Os valores são \033[31m{a}\033[m e \033[32m{b}\033[m!')

nome = 'Guanabara'
print(f'Olá! Muito prazer em te conhecer \033[4;34m{nome}\033[m!')

# Dessa forma fica com uma "," indesejada:
cores = {'limpa' : '\033[m',
         'azul' : '\033[34m',
         'amarelo': '\033[33m,',
         'pretoebranco' : '\033[7;30m'}
nome = 'Guanabara'
print(f'Olá! Muito prazer em te conhecer {cores["amarelo"]} {nome}{cores["limpa"]}!')
