import pygame, sys


class Shooter:
    """A sidyways shooter game with pygame package."""
    
    def __init__(self):
        """Initialize game screen."""
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        
        
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
        self.screen.fill((255,255,255))
        pygame.display.flip()
        
        
    
if __name__ == "__main__":
    game = Shooter()
    game.run_game()