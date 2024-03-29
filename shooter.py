import pygame, sys
from time import sleep

from settings import Settings
from jet import Jet
from bullet import Bullet
from enemy import Enemy
from random import random
from game_stats import GameStats
from text import Text
from button import Button
from scoreboard import Scoreboard


class Shooter:
    """A sidyways shooter game with pygame package."""
    
    def __init__(self):
        """Initialize game screen."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_width()
        self.settings.screen_height = self.screen.get_height()
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        
        # bullet group
        self.bullets = pygame.sprite.Group()
        # jet instance
        self.jet = Jet(self)
        
        # enemy group
        self.enemies = pygame.sprite.Group()      
        
        # end game text
        self.end_game_text = Text(self)
        
        # initialize button
        self.play_button = Button(self, "Play")
        
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_play_button(self, mouse_pos):
        """start a new game when the player clicks play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()
            
            
    def _start_game(self):
        """a method to start the game."""
            # reset game statistics
        self.stats.game_reset()
        self.sb.prep_score_image()
        self.stats.game_active = True
        
        # get rid of any remaining enemies or bullets
        self.enemies.empty()
        self.bullets.empty()
        
        # reposition jet
        self.jet.reposition()
        
        # hide the mouse cursor.
        pygame.mouse.set_visible(False)
        
            
    def _check_keydown_events(self, event):
        """check keyboard keydown events."""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_p:
            if not self.stats.game_active:
                self._start_game()
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
            # check for anamy bullet that have hit enemies.
            # if so get rid of the bullet and the enemy.
            collisions = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
            if collisions:
                self._increase_score()
                self._check_score()
                self.sb.prep_score_image()
                self._check_high_score()
            # get rid of old bullets that have disappeard.
            self._delete_old_bullet()
            
    def _check_score(self):
        """check score if the score is equal to """
        self.stats.enemies_shot_down +=1
        if self.stats.enemies_shot_down % 10 == 0:
            self.settings.increase_speed()
            self.stats.game_level +=1
            self.sb.prep_game_level_image()
            
            
    def _check_high_score(self):
        """check if score is greater than high score, the high score will be updated."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.sb.prep_high_score_image()
        
            
    def _increase_score(self):
        """to increase score point if the enemy was shot."""
        self.stats.score += self.settings.score_point
        
            
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
            
            
    def _check_hit(self):
        """check if jet or any of enemies collide"""
        if pygame.sprite.spritecollideany(self.jet, self.enemies):
            if self.stats.jet_left > 0:
                # decrement 
                self.stats.jet_left -=1
                self.sb.prep_jet_left_image()
                
                # remove remaining bullets and enemies
                self.enemies.empty()
                self.bullets.empty()
                
                # reposition the jet 
                self.jet.reposition()
                
                # pause 
                sleep(0.5)
            else:
                self.stats.game_active = False
                # set the mouse cursor visible again.
                pygame.mouse.set_visible(True)
            
            
                
    def _update_screen(self):
        """update and flip screen to the latest frame created."""
        self.screen.fill(self.settings.bg_color)
        self.sb.show_score()
        if self.stats.game_active:
            self.jet.blit_me()
            self._update_bullets()
            self.enemies.draw(self.screen)
            self.enemies.update()
            self._check_hit()
        else:
            self.screen.blit(self.end_game_text.text, self.end_game_text.text_rect)
            self.play_button.draw_button()
            self.stats.game_reset()
            self.sb.prep_score_image()
            self.sb.prep_game_level_image()
            self.sb.prep_jet_left_image()
        pygame.display.flip()
        
        
    
if __name__ == "__main__":
    game = Shooter()
    game.run_game()