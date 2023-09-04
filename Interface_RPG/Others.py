import pygame
from Interface_RPG.button_use import Button, Button_img
from Logic_RPG.ChangVariables import assign_value
from pygame.locals import *
import sys

# create in the Screen a button whith the option to close or stay in the game
def end_button( ScreenWhidth: int, ScreenHeight: int, Screen: pygame.Surface ):

    pygame.init()

    run = True

    # load img
    PanelBeige = pygame.image.load("Photos/Panel/panel_beige.png")
    PanelInsetBeigeLight = pygame.image.load("Photos/Panel/panelInset_beigeLight.png")

    # determinate the position of the buttons
    DivisionSreenWhidth = int(ScreenWhidth / 4)
    DivisionSreenHeight = int(ScreenHeight / 4)

    # rect of the board of button to end
    Rect = pygame.Rect((ScreenWhidth / 6), (ScreenHeight / 6), (6 * ScreenWhidth / 9), (6 * ScreenWhidth / 9))
    ScaledPanelBeige = pygame.transform.scale(PanelBeige, ((int(6 * ScreenWhidth / 9)), (int(( 3 * ScreenHeight / 6)))))
    
    # create the large of the font
    font = int( ( ScreenWhidth / 25 ) )
    fontd = pygame.font.SysFont('oldenglishtext', font)

    # creates the buttons
    ButEndImg = Button_img( (DivisionSreenWhidth - 20), DivisionSreenHeight , DivisionSreenWhidth, DivisionSreenHeight, (255,255,0), "Exit Game", (255,0,0), action = lambda: finish_game() )
    ButErrorImg = Button_img( (2*DivisionSreenWhidth +20), DivisionSreenHeight , DivisionSreenWhidth, DivisionSreenHeight, (255,255,0), "Continue", (255,0,0), action = lambda: assign_value() )

    # start the loop
    while(run):

        # wait the event
        for event in pygame.event.get():

            # proces the event in the buttons            
            ButEndImg.handle_event_img(event)
            running = ButErrorImg.handle_event_img(event)

            # valid the event in the button error
            if running != None:
                run = running

        # draw the button on the screen 
        Screen.blit(ScaledPanelBeige, (int((ScreenWhidth / 6)), int((ScreenHeight / 6))))
        ButEndImg.draw_img(Screen,fontd)
        ButErrorImg.draw_img(Screen,fontd)
        

        # update te screen in real time
        pygame.display.flip()

# create in the Screen a button whith the option to close game, stay in the game, back to the title and save game
def end_button_runing( ScreenWhidth: int, ScreenHeight: int, Screen: pygame.Surface ):

    pygame.init()

    run = True

    # load img
    PanelBeige = pygame.image.load("Photos/Panel/panel_beige.png")
    PanelInsetBeigeLight = pygame.image.load("Photos/Panel/panelInset_beigeLight.png")

    # determinate the position of the buttons
    DivisionSreenWhidth = int(ScreenWhidth / 4)
    DivisionSreenHeight = int(ScreenHeight / 6)

    # rect of the board of button to end
    Rect = pygame.Rect((ScreenWhidth / 6), (ScreenHeight / 6), (6 * ScreenWhidth / 9), (6 * ScreenWhidth / 9))
    ScaledPanelBeige = pygame.transform.scale(PanelBeige, ((int(6 * ScreenWhidth / 9)), (int(( 3 * ScreenHeight / 6)))))
    
    # create the large of the font
    font = int( ( ScreenWhidth / 25 ) )
    fontd = pygame.font.SysFont('oldenglishtext', font)

    # creates the buttons
    ButEndImg = Button_img( (DivisionSreenWhidth - 20), (7/5*DivisionSreenHeight) , DivisionSreenWhidth, DivisionSreenHeight, (255,255,255), "Exit Game", (255,255,255), action = lambda: finish_game() )
    ButErrorImg = Button_img( (2*DivisionSreenWhidth +20), (7/5*DivisionSreenHeight) , DivisionSreenWhidth, DivisionSreenHeight, (255,255,255), "Continue", (255,255,255), action = lambda: assign_value() )
    ButBackTitle = Button_img( (2*DivisionSreenWhidth +20), (13/5*DivisionSreenHeight) , DivisionSreenWhidth, DivisionSreenHeight, (255,255,255), "Back", (255,255,255), action = lambda: assign_value() )
    # start the loop
    while(run):

        # wait the event
        for event in pygame.event.get():

            # proces the event in the buttons            
            ButEndImg.handle_event_img(event)
            running = ButErrorImg.handle_event_img(event)
            runing = ButBackTitle.handle_event_img(event)

            # valid the event in the button error
            if running != None:
                run = running
            
            # valid the event in the button back
            if runing != None:
                return False

        # draw the button on the screen 
        Screen.blit( ScaledPanelBeige, (int((ScreenWhidth / 6)), int((ScreenHeight / 6))) )
        ButEndImg.draw_img( Screen, fontd )
        ButErrorImg.draw_img( Screen, fontd )
        ButBackTitle.draw_img( Screen, fontd )
        

        # update te screen in real time
        pygame.display.flip()



# thats funcion ends the program
def finish_game():

    pygame.quit()
    sys.exit()

# this def change the fullscreen mode
def assign_fullscreen( Full: str ) -> str:

    if Full == "Window":
        Full = "Fullscreen"
        pygame.display.toggle_fullscreen()
    else:
        Full = "Window"
        pygame.display.toggle_fullscreen()
    
    return Full