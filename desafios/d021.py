'''
Desafio 021
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''

import pygame # Usar "pip install pygame" no terminal se ainda não instalada essa biblioteca.

pygame.init() # Iniciando o "Pygame".

pygame.mixer.music.load('d021.mp3') # Caminho do arquivo .mp3.
pygame.mixer.music.play()
pygame.event.wait()
