import pygame


class Jet:
    """a class to represent jet object on the screen."""
    
    def __init__(self, game):
        """initialize jet rect and set screen size."""
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        
        # load jet image
        self.image = pygame.image.load("images/jet.bmp")
        self.rect = self.image.get_rect()
        
        # set image position
        self.rect.midleft = self.screen_rect.midleft
        
        # set image y to float value
        self.y = float(self.rect.y)
        # set jet direction
        self.moving_up = False
        self.moving_down = False
        
        
        
    def blit_me(self):
        """draw image to the screen."""
        self.screen.blit(self.image ,self.rect)
    
    
    def update(self):
        """update jet position on screen."""
        if self.moving_up and (self.rect.top >=0):
            self.y -= self.settings.jet_speed
        if self.moving_down and (self.rect.bottom <= self.screen_rect.bottom):
            self.y += self.settings.jet_speed
        
        self.rect.y = self.y
        