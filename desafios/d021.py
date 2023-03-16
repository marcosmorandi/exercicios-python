'''
Desafio 021
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''

import pygame

# inicializa o pygame
pygame.init()

# carrega o arquivo de áudio
pygame.mixer.music.load("d021.mp3")

# reproduz o arquivo de áudio
pygame.mixer.music.play()

# espera a reprodução do áudio terminar
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

# para a reprodução do áudio
pygame.mixer.music.stop()
