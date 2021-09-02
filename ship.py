import pygame


class Ship():
    def __init__(self, ai_games):
        self.screen = ai_games.screen
        self.screen_rect = ai_games.screen.get_rect()

        self.image = pygame.image.load('img/ship.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = sels.screen_rect.midbottom

    def blitme(self):
        self.screen.bilt(self.image, self.rect)
