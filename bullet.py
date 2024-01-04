from pygame.sprite import Sprite
import pygame
class Bullet(Sprite):
    """a class to represent bullet object on screen."""
    
    def __init__(self, game):
        """initialize screen rect and make bullet rect"""
        super().__init__()
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        
        # set bullet color 
        self.color = self.settings.bullet_color
        
        # load bullet rect 
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        # set bullet position
        self.rect.midleft = game.jet.rect.midleft
        
        # save position as decimal value
        self.x = float(self.rect.x)
        
    def update(self):
        """update the bullet x position."""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x
        
    def draw_bullet(self):
        """draw bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
        
    def pass_edge(self):
        """deletes old bullet if pass through edge."""
        if self.rect.left > self.screen_rect.right:
            return True
            
            