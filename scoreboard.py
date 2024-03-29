import pygame.font
from jet import Jet


class Scoreboard:
    """scoreboard system to display all game scores on screen."""
    
    
    def __init__(self, game):
        """to initialize scoreboard"""
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats
        
        self.font_color = (60, 60, 60)
        self.font = pygame.font.SysFont(None, 48)
        
        self.prep_score_image()
        self.prep_high_score_image()
        self.prep_game_level_image()
        self.prep_jet_left_image()
        
    def prep_score_image(self):
        """prepare score image """
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,
                                            self.font_color, self.settings.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.top = self.screen_rect.top + 10
        self.score_image_rect.right = self.screen_rect.right - 20
        
    def prep_high_score_image(self):
        """prepare high score image."""
        high_score_str = str(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.font_color, self.settings.bg_color)
        self.high_score_image_rect = self.high_score_image.get_rect()
        self.high_score_image_rect.top = self.score_image_rect.top
        self.high_score_image_rect.centerx = self.screen_rect.centerx
        
    def prep_game_level_image(self):
        """prepare game level image."""
        game_level_str = str(self.stats.game_level)
        self.game_level_image = self.font.render(game_level_str, True,
                                          self.font_color, self.settings.bg_color)
        self.game_level_image_rect = self.game_level_image.get_rect()
        self.game_level_image_rect.top = self.score_image_rect.top + 50
        self.game_level_image_rect.right = self.score_image_rect.right
        
    def prep_jet_left_image(self):
        """prepare jet left image."""
        self.game.jets = pygame.sprite.Group()
        for jet_num in range(self.stats.jet_left):
            new_jet = Jet(self.game)
            new_jet.rect.top = self.high_score_image_rect.top
            new_jet.rect.left = self.screen_rect.left + new_jet.rect.width * jet_num
            self.game.jets.add(new_jet)

        
        
    
    def show_score(self):
        """display score images on screen"""
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.high_score_image, self.high_score_image_rect)
        self.screen.blit(self.game_level_image, self.game_level_image_rect)
        self.game.jets.draw(self.screen)