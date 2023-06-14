import sys
import time
import pygame
from pygame.sprite import Group

from settings import Settings
import game


def run_game():
        # Иницилизирует игру и создает объект экрана.
        pygame.init()
        ai_settings = Settings()
        screen = pygame.display.set_mode((ai_settings.scr_width, ai_settings.scr_height))
        pygame.display.set_caption("Alien Invasion")

        #Создание группы для звезд
        stars = Group()
        game.create_fleet(ai_settings, screen, stars)
        # Запуск основного цикла игры.
        while True:
            game.check_events()
            game.update_stars(stars)
            game.update_screen(ai_settings, screen, stars)



run_game()