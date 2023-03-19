'''
Desafio 021 - Feito
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''

# Usar o "playsound". Funcionou no VSCode Portable .mp3 com 128kbps e 320kbps.
# Cuidar a quantidade e tipo de caracteres no nome. Testar com calma.

from playsound import playsound

# Caminho do arquivo de áudio.
path = '.\media\Bibio-Lovers_Carvings.mp3'

# Reproduz o arquivo de áudio.
playsound(path)
