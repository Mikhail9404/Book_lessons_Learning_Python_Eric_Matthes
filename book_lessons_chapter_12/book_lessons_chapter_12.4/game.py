import sys
import pygame


from settings import Settings
from rocket import Rocket

class TestGame:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Test Game")

        self.rocket = Rocket(self)
        self.bg_color = (230, 230, 230)


    def run_game(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    tg = TestGame()
    tg.run_game()