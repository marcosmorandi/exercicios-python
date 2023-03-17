'''
Desafio 021 - Feito
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''

# Usar o "playsound". Funcionou no VSCode Portable .mp3 com 128kbps e 320kbps.
# Cuidar a quantidade e tipo de caracteres no nome. Testar com calma.

from playsound import playsound

# caminho do arquivo de áudio
path = "desafios\Bibio-lovers_carvings.mp3"

# reproduz o arquivo de áudio
playsound(path)
