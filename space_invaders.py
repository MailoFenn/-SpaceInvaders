import sys
import pygame

from settings import Settings
from ship import Ship

# комент для теста


class SpaceInvaders:
    def __init__(self):
        """Инициализация экрана игры и настройки."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Space Invaders")

        self.ship = Ship(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            pygame.display.flip()


if __name__ == '__main__':
    si = SpaceInvaders()
    si.run_game()
