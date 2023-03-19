'''
Exercício 021 - Feito
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''

# Usar o "Pygame".

# Importando o "Pygame".
import pygame

# Inicializando o "mixer" do "Pygame". Tem que ser nessa ordem, primeiro "mixer" depois "Pygame".
pygame.mixer.init()

# Inicializando o "Pygame".
pygame.init()

# No VSCode usar o ".\" para indicar o caminho do arquivo ".mp3".
pygame.mixer.music.load('.\media\Bibio-Lovers_Carvings.mp3')
pygame.mixer.music.play()
pygame.event.wait()
