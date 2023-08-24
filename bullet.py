import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.Thescreen = ai_game.Thescreen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
            self.settings.bullet_height)
        self.rect.topleft = ai_game.ship.rect.topleft

        self.y = float(self.rect.y)
    
    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.Thescreen, self.color, self.rect)
