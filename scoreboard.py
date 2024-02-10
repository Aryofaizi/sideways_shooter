import pygame.font
class Scoreboard:
    """scoreboard system to display all game scores on screen."""
    
    
    def __init__(self, game):
        """to initialize scoreboard"""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats
        
        self.font_color = (60, 60, 60)
        self.font = pygame.font.SysFont(None, 48)
        
        self.prep_score_image()
        
    def prep_score_image(self):
        """prepare score image """
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,
                                            self.font_color, self.settings.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.top = self.screen_rect.top + 10
        self.score_image_rect.right = self.screen_rect.right - 20
        
    
    def show_score(self):
        """display score images on screen"""
        self.screen.blit(self.score_image, self.score_image_rect)
        
    