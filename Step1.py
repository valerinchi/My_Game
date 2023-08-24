import sys

import pygame

from settings import Settings
from Step2 import The_Ship
from bullet import Bullet

class TheAlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.Thescreen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.Thescreen_width = self.Thescreen.get_rect().width
        self.settings.Thescreen_lenght= self.Thescreen.get_rect().height
        pygame.display.set_caption("The Alien Invasion")

        self.ship = The_Ship(self)
        self.bullets = pygame.sprite.Group()
    
    def run_the_game(self):
        while True:
            self._check_TheEvents()
            self.ship.The_Update()
            self._update_bullets()
            self._update_TheScreen()
            self.clock.tick(60)
    
    def _check_TheEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    sys.exit()   
            elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
             sys.exit()
        elif event.key == pygame.K_SPACE:
             self._fire_bullet()
     
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False  
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)
                
    def _update_TheScreen(self):
        self.Thescreen.fill(self.settings.The_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()

        pygame.display.flip()
          
if __name__ == '__main__':
    ai = TheAlienInvasion()
    ai.run_the_game()
  
                 
             