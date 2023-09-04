import pygame
from pygame.locals import *
import sys

# this .py it has a def to move the characters the map and others things

# move the map on the screen and move the character when you prees wasd  
def Move_map( move_x: int, move_y: int, move_speed: int ) -> tuple[int,int]:

    keyboard = pygame.key.get_pressed()

    if keyboard[pygame.K_w]:
        move_y += move_speed
    elif keyboard[pygame.K_s]:
        move_y -= move_speed
    elif keyboard[pygame.K_d]:
        move_x -= move_speed
    elif keyboard[pygame.K_a]:
        move_x += move_speed

    return move_x, move_y 