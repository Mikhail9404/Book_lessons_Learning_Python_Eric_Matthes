import pygame

class Rocket():

    def __init__(self, tg_game):
        self.screen = tg_game.screen
        self.settings = tg_game.settings
        self.screen_rect = tg_game.screen.get_rect()

        self.image = pygame.image.load('character/picture.bmp')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
