import sys

import pygame

class TheAlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.Thescreen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("The Alien Invasion")

        self.the_color = (77, 26, 127)
    
    def run_the_game(self):
        while True:
            for the_event in pygame.event.get():
                if the_event.type == pygame.QUIT:
                    sys.exit()

            self.Thescreen.fill(self.the_color)
            
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    ai = TheAlienInvasion()
    ai.run_the_game()