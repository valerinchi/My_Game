import pygame

class The_Ship:
    def __init__(self, ai_game):
        self.Thescreen = ai_game.Thescreen
        self.settings = ai_game.settings
        self.Thescreen_rect = ai_game.Thescreen.get_rect()

        self.image = pygame.image.load('image/Ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.center = self.Thescreen_rect.center
        

        self.x = float(self.rect.x)
        
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def The_Update(self):
        if self.moving_right and self.rect.right < self.Thescreen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.Thescreen_rect.bottom:
            self.rect.y += self.settings.ship_speed
        
        self.rect.x = self.x

    def blitme(self):
        self.Thescreen.blit(self.image, self.rect)

