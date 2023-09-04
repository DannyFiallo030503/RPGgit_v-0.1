import pygame
from pygame.locals import *
from Interface_RPG.Others import finish_game, end_button, end_button_runing

def load_game( ScreenWhidth: int, ScreenHeight: int, Screen: pygame.Surface ):

    run = True

    pygame.init()

    while(run):

        Screen.fill( (200,200,200) )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    runing = end_button_runing( ScreenWhidth, ScreenHeight, Screen )
                    if runing != None:
                        run = runing
                
        pygame.display.flip()