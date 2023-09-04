import pygame
from Interface_RPG.button_use import Button, Button_img
from Interface_RPG.Others import end_button, finish_game
from pygame.locals import *
from Interface_RPG.Running_Game import running_game
from Interface_RPG.Create_Game import create_game
from Interface_RPG.Load_Game import load_game
from Interface_RPG.Config import config
import sys
import ctypes


# start the game whith a screen option to ccreate a new world, load word...
# to do:
# start whith a introdicin screen: the creator, presentation and maybe a video

pygame.init()

# colors
sky_color = (135, 206, 235)
ground_color = (34, 139, 34)
sun_color = (255, 255, 0)
a = (244,350,3)

# take the fullscreen on you computer 
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
ScreenWhidth, ScreenHeight = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

DivScreenWhidth = ScreenWhidth / 10
DivScreenHeight = ScreenHeight / 14

font = int( ( ScreenWhidth / 30 ) )
fontd = pygame.font.SysFont('oldenglishtext', font) # rockwell,oldenglishtext,blackadderitc,parchment

# create the screen
Screen = pygame.display.set_mode( (ScreenWhidth, ScreenHeight) )

# buttons
ContinueButton = Button_img( (4 * DivScreenWhidth), (2 * DivScreenHeight), (2 * DivScreenWhidth), (2 * DivScreenHeight), (255,255,0), "Continue", (255,255,255), action = lambda: running_game( ScreenWhidth, ScreenHeight, Screen ) )
NewGameButton = Button_img( (4 * DivScreenWhidth), (5 * DivScreenHeight), (2 * DivScreenWhidth), (2 * DivScreenHeight), (255,255,0), "New Game", (255,255,255), action = lambda: create_game( ScreenWhidth, ScreenHeight, Screen ) )
LoadGameButton = Button_img( (4 * DivScreenWhidth), (8 * DivScreenHeight), (2 * DivScreenWhidth), (2 * DivScreenHeight), (255,255,0), "Load Game", (255,255,255), action = lambda: load_game( ScreenWhidth, ScreenHeight, Screen ) )
ConfGameButton = Button_img( (4 * DivScreenWhidth), (11 * DivScreenHeight), (2 * DivScreenWhidth), (2 * DivScreenHeight), (255,255,0), "Configure", (255,255,255), action = lambda: config( ScreenWhidth, ScreenHeight, Screen ) )

# start the music
pygame.mixer.music.load("Soundtrack/prologue.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1) # change the volume 0.0 is the low volume and 1.0 is the max

# start the loop
Run = True
while(Run):

    # draw the single color in the screen
    # to do:
    # create a font of the inicial screen, something epic... maybe
    Screen.fill( (200,200,200) )

    # drawing the inicial screen
    Screen.fill(sky_color)
    pygame.draw.rect(Screen, ground_color, pygame.Rect(0, 540, 1920, 540))
    pygame.draw.circle(Screen, sun_color, (100, 100), 50)

    # procese the event
    for event in pygame.event.get():
            
        # condicional when the event is the "X" of quit
        if event.type == pygame.QUIT:
            finish_game()

        # conditional when the event is a Key
        elif event.type == KEYDOWN:
                
            # condicional when the event is Esc from the keyboard
            if event.key == K_ESCAPE:
                end_button( ScreenWhidth, ScreenHeight, Screen )
        
        # proces event to the buttons
        ConfGameButton.handle_event_img(event)
        ContinueButton.handle_event_img(event)
        NewGameButton.handle_event_img(event)
        LoadGameButton.handle_event_img(event)

    # draw the buttons  
    ConfGameButton.draw_img(Screen,fontd)
    ContinueButton.draw_img(Screen,fontd)
    NewGameButton.draw_img(Screen,fontd)
    LoadGameButton.draw_img(Screen,fontd)


    # upgrade the screen 
    pygame.display.flip()               

pygame.quit()


