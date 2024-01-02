import pygame, sys
from settings import Settings
from jet import Jet


class Shooter:
    """A sidyways shooter game with pygame package."""
    
    def __init__(self):
        """Initialize game screen."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_width()
        self.settings.screen_height = self.screen.get_height()
        
        # jet instance
        self.jet = Jet(self)
        
    def run_game(self):
        """Method to run the game."""
        while True:
            # main game loop
            self._check_events()
            self._update_screen()
        
    def _check_events(self):
        """check keyboard keydown and keyup events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydow_events(event)
    def _check_keydow_events(self, event):
        """check keyboard keydown events."""
        if event.key == pygame.K_q:
            sys.exit()
            
    def _update_screen(self):
        """update and flip screen to the latest frame created."""
        self.screen.fill(self.settings.bg_color)
        self.jet.blit_me()
        pygame.display.flip()
        
        
    
if __name__ == "__main__":
    game = Shooter()
    game.run_game()