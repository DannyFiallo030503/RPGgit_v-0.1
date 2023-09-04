import pygame
from pygame.locals import *


def show_map(map,DISPLAY,ScaleImgGrass,ScaleImgRock,ScaleImgNone,grid_x,cell_size,grid_y):
    if map!=None:
        for i in range(0,len(map)):
            for j in range(0,len(map[i])):
                if map[i][j]=='1':
                    DISPLAY.blit(ScaleImgGrass, (grid_x + j * cell_size, grid_y + i * cell_size))
                elif map[i][j]=='2':
                    DISPLAY.blit(ScaleImgRock, (grid_x + j * cell_size, grid_y + i * cell_size))
                elif map[i][j]=='0':
                    DISPLAY.blit(ScaleImgNone, (grid_x + j * cell_size, grid_y + i * cell_size))