import pygame
from pygame.locals import *
from Interface_RPG.Others import finish_game, end_button, assign_fullscreen, end_button_runing
from Interface_RPG.button_use import Button_img
from Logic_RPG.Settings import select_resolution
from Logic_RPG.ChangVariables import assign_value

# this's the configure of the game, Type of screen(window,fullscreen), volumen and mouse/keyboard
# to do:
# change the posibiliti to assing the keyboard or click you whant in you game
def config( ScreenWhidth: int, ScreenHeight: int, Screen: pygame.Surface ):

    # variables
    Run = True
    Running = None
    ControlFull = None 
    Full = "Fullscreen"

    pygame.init()
    
    # Loop start
    while(Run):

        ScreenWhidthHeight = [ScreenWhidth, ScreenHeight]

        DevScreenWhidth = ScreenWhidth / 20
        DevScreenHeight = ScreenHeight / 20

        # create the fontd of the text
        font = int( ( ScreenWhidth / 30 ) )
        fontd = pygame.font.SysFont('Yu Gothic UI Semibold', font)
        TextResolution = fontd.render((str(ScreenWhidth)+'x'+str(ScreenHeight)), True, (255, 255, 255))
        TextRectResolution = TextResolution.get_rect()
        TextRectResolution.center = ( (11 * DevScreenWhidth), (3 * DevScreenHeight) )
        TextFullscreen = fontd.render( str(Full), True, (255, 255, 255) )
        TextRectFullscreen = TextFullscreen.get_rect()
        TextRectFullscreen.center = ( (11 * DevScreenWhidth), (6 * DevScreenHeight) )

        # create the buttons
        ButResolution = Button_img( (2 * DevScreenWhidth), (2 * DevScreenHeight), (6 * DevScreenWhidth), (2 * DevScreenHeight), (255,200,255), "Resolution", (255,255,255), action = lambda: select_resolution( ScreenWhidthHeight ) )
        ButFullScreen = Button_img( (2 * DevScreenWhidth), (6 * DevScreenHeight), (6 * DevScreenWhidth), (2 * DevScreenHeight), (255,200,255), Full, (255,255,255), action = lambda: assign_fullscreen( Full ) )
        ButBack = Button_img( (2 * DevScreenWhidth), (16 * DevScreenHeight), (6 * DevScreenWhidth), (2 * DevScreenHeight), (255,200,255), "Back", (255,255,255), action = lambda: assign_value() )
        #ButVolMusic =

        Screen.fill( (200,200,200) )

        # proces the event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    runing = end_button_runing( ScreenWhidth, ScreenHeight, Screen )
                    if runing != None:
                        Run = runing
            # proces the event button
            # the button of the type of the screen
            ControlFull = ButFullScreen.handle_event_img(event)
            if ControlFull != None:
                Full = ControlFull
            # the button of the resolution on the screen
            ButResolution.handle_event_img(event)
            if ScreenHeight != ScreenWhidthHeight[1]:
                screen_width = pygame.display.Info().current_w
                screen_height = pygame.display.Info().current_h
                window_x = (screen_width - ScreenWhidth) // 2
                window_y = (screen_height - ScreenHeight) // 2
                window_pos = (window_x, window_y)
                pygame.display.toggle_fullscreen()
                ScreenWhidth = ScreenWhidthHeight[0]
                ScreenHeight = ScreenWhidthHeight[1]
                ScreenWhidthHeight = [ScreenWhidth, ScreenHeight]
                Screen = pygame.display.set_mode( (ScreenWhidth, ScreenHeight), pygame.RESIZABLE )
            # the button of back
            Running = ButBack.handle_event_img(event)
            if Running != None:
                Run = Running

        # draw the buttons
        ButFullScreen.draw_img( Screen, fontd )
        ButResolution.draw_img( Screen, fontd )
        ButBack.draw_img( Screen, fontd )
        # draw the resolition the game
        pygame.draw.rect( Screen, (0, 0, 0), TextRectResolution )
        Screen.blit( TextResolution, TextRectResolution )
             
        pygame.display.flip()