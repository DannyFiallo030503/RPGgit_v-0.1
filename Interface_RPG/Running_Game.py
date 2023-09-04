import pygame
from pygame.locals import *
from Interface_RPG.Others import finish_game,end_button, end_button_runing
from Interface_RPG.Show import show_map
from Logic_RPG.Maps import maps_game
from Logic_RPG.Move import Move_map
import sys


def running_game( ScreenWhidth: int, ScreenHeight: int, Screen: pygame.Surface ):

    run = True
    move_x = 0
    move_y = 0
    move_speed = 10

    pygame.init()

    mapinit = maps_game()

    ScaleScreenWhidth = ScreenWhidth / 5
    SclaleScreenHeight = ScreenHeight / 5

    ImgGrass = pygame.image.load("Photos/Objects/Floor-07-07.png")
    ImgRock = pygame.image.load("Photos/Objects/Floor-01-07.png")
    ImgNone = pygame.image.load("Photos/Objects/grassgreen.png")
    ScaleImgGrass = pygame.transform.scale(ImgGrass,(160,160))
    ScaleImgRock = pygame.transform.scale(ImgRock,(160,160))
    ScaleImgNone = pygame.transform.scale(ImgNone,(160,160))

    while(run):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    runing = end_button_runing( ScreenWhidth, ScreenHeight, Screen )
                    if runing != None:
                        run = runing

        move_x, move_y = Move_map( move_x, move_y, move_speed )

        show_map(mapinit,Screen,ScaleImgGrass,ScaleImgRock,ScaleImgNone,move_x,160,move_y)
                
        pygame.display.flip()