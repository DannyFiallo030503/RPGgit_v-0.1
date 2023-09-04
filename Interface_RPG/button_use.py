import pygame
import sys

# This Class create the button  
class Button:
    def __init__( self, x, y, width, height, color, text, text_color, action = None ):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.action = action

    # draw the button
    def draw(self, surface, fontd):
        pygame.draw.rect(surface, (50, 50, 50), self.rect.move(6, 6))
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect( surface, self.color, self.rect )
        text = fontd.render( self.text, True, self.text_color )
        text_rect = text.get_rect( center = self.rect.center )
        surface.blit( text, text_rect )
        pygame.draw.rect(surface, (200, 100, 200), self.rect, 4)

    # handle the event
    def handle_event( self, evente ):
        if evente.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint( evente.pos ):
            if self.action:
                return self.action()
        return None
    
# this class create teh button with a imagens
class Button_img:
    def __init__( self, x, y, width, height, color, text, text_color, action = None ):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.action = action
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # draw the button
    def draw_img(self, surface, fontd):
        buttonLong_blue = pygame.image.load( "Photos/Panel/buttonLong_blue.png" )
        scaled_image = pygame.transform.scale( buttonLong_blue, ( self.width, self.height ) )
        surface.blit( scaled_image,( self.x, self.y ) )
        text = fontd.render( self.text, True, self.text_color )
        text_rect = text.get_rect( center = self.rect.center )
        surface.blit( text, text_rect )

    # handle the event
    def handle_event_img( self, evente ):
        if evente.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint( evente.pos ):
            if self.action:
                Sound1 = pygame.mixer.Sound("soundtrack/Audio/bookFlip2.ogg")
                Sound1.play()
                return self.action()
        return None
    
# Class to input text
class TextInput:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = pygame.Color('gray')
        self.text = ''
        self.font = pygame.font.Font(None, 32)
        self.active = False

    def handle_event_textinput(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)  # aquí puedes hacer algo con el texto ingresado
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw_textinput(self, screen):
        txt_surface = self.font.render(self.text, True, self.color)
        width = max(self.rect.width, txt_surface.get_width() + 10)
        self.rect.width = width
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(txt_surface, (self.rect.x + 5, self.rect.y + 5))

# class number input
class NumberInput:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = pygame.Color('gray')
        self.text = ''
        self.font = pygame.font.Font(None, 32)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    if self.text.isdigit():
                        print(int(self.text))  # aquí puedes hacer algo con el número ingresado
                        self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.unicode.isdigit():
                    self.text += event.unicode

    def draw(self, screen):
        txt_surface = self.font.render(self.text, True, self.color)
        width = max(self.rect.width, txt_surface.get_width() + 10)
        self.rect.width = width
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(txt_surface, (self.rect.x + 5, self.rect.y + 5))