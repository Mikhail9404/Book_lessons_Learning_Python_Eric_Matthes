import sys
import pygame

class Game():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Test Game")
        self.bg_color = (230, 230, 230)


    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)


    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            print(event.key)
        elif event.key == pygame.K_LEFT:
            print(event.key)
        elif event.key == pygame.K_DOWN:
            print(event.key)
        elif event.key == pygame.K_UP:
            print(event.key)
        elif event.key == pygame.K_q:
            sys.exit()


    def _update_screen(self):
        pygame.display.flip()

if __name__ == '__main__':
    tg = Game()
    tg.run_game()