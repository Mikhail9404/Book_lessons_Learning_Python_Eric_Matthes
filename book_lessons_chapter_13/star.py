import pygame

from pygame.sprite import Sprite

class Star(Sprite):
    #Класс предстовляющий одну звезду
    def __init__(self, ai_settings, screen):
        super(Star, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Загрузка изображения звезды
        self.image = pygame.image.load('images/water.jpg')
        self.rect = self.image.get_rect()

        #Каждая новая звезда появляется в левом верхнем углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Сохранение позиции
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def check_edges(stars, screen):
        scr_rect = screen.get_rect()
        if stars.rect.top >= scr_rect.y:
            return True


    def update(self):
        self.y += self.ai_settings.img_speed_factor
        self.rect.y = self.y


    def blitme(self):
        #Выводит звезду на экран
        self.screen.blit(self.image, self.rect)