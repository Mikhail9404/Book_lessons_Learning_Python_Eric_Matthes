import pygame

class Character():

    def __init__(self, test_game):
        self.screen = test_game.screen
        self.screen_rect = test_game.screen.get_rect()

        self.image = pygame.image.load('character/istockphoto-1488426094-612x612.bmp')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        
        self.rect.center = self.screen_rect.center
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)