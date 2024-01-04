from pygame.sprite import Sprite
import pygame


class Enemy(Sprite):
    """a class to represent alien object on screen."""
    
    def __init__(self, game):
        """initialize game screen and create enemy image."""
        super().__init__()
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        
        
        # load alien image and rect
        self.image = pygame.image.load("images/enemy.bmp")
        self.rect = self.image.get_rect()
        # set image position
        self.rect.topright = self.screen_rect.topright
    
    
    def blit_me(self):
        """draw enemy to the screen."""
        self.image.blit(self.screen, self.rect)