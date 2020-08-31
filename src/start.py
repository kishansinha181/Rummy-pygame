import pygame
from pygame.locals import *


pygame.init()

screen = pygame.display.set_mode((1500,750))

pygame.mixer.music.load('casino_sound.mp3')
pygame.mixer.music.play(-1)

play = True

while play:


    screen.blit(pygame.image.load('Image/intro.png'),(0,0))
    
    
    for event in pygame.event.get():
        if event.type==KEYDOWN and event.key ==ord('p'):
            pygame.mixer.music.stop()
            import game_rummy


        if event.type==KEYDOWN and event.key ==ord('q'):
                play = False 
                

        if event.type == pygame.QUIT:
                play = False

    pygame.display.update()

