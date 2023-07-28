import pygame

class The_Ship:
    def __init__(self, ai_game):
        self.Thescreen = ai_game.Thescreen
        self.Thescreen_rect = ai_game.Thescreen.get_rect()

        self.image = pygame.image.load('image/Astronaut.bmp')
        self.rect = self.image.get_rect()

        self.rect.center = self.Thescreen_rect.center

    def blitme(self):
        self.Thescreen.blit(self.image, self.rect)

