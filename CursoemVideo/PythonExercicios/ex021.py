'''
FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA AUDIO
DE UM ARQUIVO MP3
'''


import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
#pygame.event.wait()   ====até aqui, aula com guanabara==
#seguindo daqui, aula com Copilot
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)














