from pygame.sprite import Sprite
import pygame
from random import randint


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
        # set image position at the right side of screen
        self.rect.left = self.screen_rect.right
        # The farthest down the screen we'll place the alien is the height
        #   of the screen, minus the height of the alien.
        
        top_max_height = self.screen_rect.height - self.rect.height
        self.rect.top = randint(0,top_max_height)
        
        
        # save enemy y as float number
        self.y = float(self.rect.y)
        self.rect.y = self.y
        
        self.x = float(self.rect.x)
        self.rect.x = self.x
        
    def update(self):
        """move enemy from right side of screen to the left side by x coordinate"""
        self.x -= self.settings.enemy_speed
        self.rect.x = self.x