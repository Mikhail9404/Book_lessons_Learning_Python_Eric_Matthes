import sys
import pygame
from star import Star


def check_events():
    #Обрабатывает нажатия клавиш и события мыши
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, stars):
    #При каждом проходе перерисовывается экран
    screen.fill(ai_settings.bg_color)
    stars.draw(screen)
    # Отображение последнего прорисованного экрана
    pygame.display.flip()

def get_number_stars_x(ai_settings, star_width):
    #Вычисление количества звезд в ряду
    number_stars_x = int(ai_settings.scr_width / star_width)
    return number_stars_x


def get_number_rows(ai_settings, star_height):
    #Вычисление количества рядов звезд
    number_rows = int(ai_settings.scr_height / star_height)
    return number_rows


def create_star(ai_settings, screen, stars, star_number, row_number):
    #Создание пришельца
    star = Star(ai_settings, screen)
    star.rect.x = star.rect.width * star_number
    star.rect.y = star.rect.height * row_number
    stars.add(star)


def create_fleet(ai_settings, screen, stars):
    #Создает флот пришельцев
    star = Star(ai_settings, screen)
    number_stars_x = get_number_stars_x(ai_settings, star.rect.width)
    number_rows = get_number_rows(ai_settings, star.rect.height)
    print(number_stars_x, number_rows, star.rect.width, star.rect.height)
    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            create_star(ai_settings, screen, stars, star_number, row_number)


def update_stars(stars):
    stars.update()