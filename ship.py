import pygame


class Ship:
    def __init__(self, ai_games):
        self.screen = ai_games.screen
        self.screen_rect = ai_games.screen.get_rect()
        self.settings = ai_games.settings

        self.image = pygame.image.load('img/ship.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.x < (self.screen_rect.right -
                                           self.rect.width):
            self.x += self.settings.ship_speed
        elif self.moving_left and self.x > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
