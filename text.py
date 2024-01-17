import pygame
class Text:
    """show text on screen."""
    
    def __init__(self, ai_game):
        """initializing a text to show on game screen."""
        self.screen = ai_game.screen
        #set font color
        self.color = (255, 0, 0)
        self.bg = (255, 255, 255)
        
        # set font 
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        
        # render the text
        self.text = self.font.render("You Lost!", True, self.color, self.bg)
        
        # create text rect
        self.text_rect = self.text.get_rect()
        
        # set rect position
        self.text_rect.center = self.screen.get_rect().center
        