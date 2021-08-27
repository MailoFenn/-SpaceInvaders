import sys
import pygame


class SpaceInvaders:
    def __init__(self):
        """Инициализация экрана игры и настройки."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Space Invaders")

        self.bg_color = (30, 30, 30)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)

            pygame.display.flip()


if __name__ == '__main__':
    si = SpaceInvaders()
    si.run_game()
