import pygame, sys
from settings import Settings
from jet import Jet
from bullet import Bullet
from enemy import Enemy
from random import random


class Shooter:
    """A sidyways shooter game with pygame package."""
    
    def __init__(self):
        """Initialize game screen."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_width()
        self.settings.screen_height = self.screen.get_height()
        
        # bullet group
        self.bullets = pygame.sprite.Group()
        # jet instance
        self.jet = Jet(self)
        
        # enemy group
        self.enemies = pygame.sprite.Group()        
        
    def run_game(self):
        """Method to run the game."""
        while True:
            # main game loop
            self._check_events()
            
            # create enemies
            self._create_enemy()    
            
            self.jet.update()
            self._update_screen()
            
        
    def _check_events(self):
        """check keyboard keydown and keyup events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self, event):
        """check keyboard keydown events."""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_DOWN:
            self.jet.moving_down = True
        elif event.key == pygame.K_UP:
            self.jet.moving_up = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
            
    def _fire_bullet(self):
        """create new bullet and add to new bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        
    def _delete_old_bullet(self):
        """get rid of """
        for bullet in self.bullets.copy():
            if bullet.pass_edge():
                self.bullets.remove(bullet)
            
    def _update_bullets(self):
        """update bullets position and count on screen."""
        # bullets position 
        self.bullets.update()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            # get rid of old bullets that have disappeard.
            self._delete_old_bullet()
        
            
    def _check_keyup_events(self, event):
        """check keyboard keyup events"""
        if event.key == pygame.K_DOWN:
            self.jet.moving_down = False
        elif event.key == pygame.K_UP:
            self.jet.moving_up = False
    
    def _create_enemy(self):
        if random() < self.settings.enemy_freqeuncy:
            new_enemy = Enemy(self)
            self.enemies.add(new_enemy)
            
                
    def _update_screen(self):
        """update and flip screen to the latest frame created."""
        self.screen.fill(self.settings.bg_color)
        self.jet.blit_me()
        self._update_bullets()
        self.enemies.draw(self.screen)
        self.enemies.update()
            
        pygame.display.flip()
        
        
    
if __name__ == "__main__":
    game = Shooter()
    game.run_game()