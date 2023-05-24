import pygame, sys
from charecter import Character

class TestGame():

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 900))
        pygame.display.set_caption("Test Game")

        self.bg_color = (30, 144, 255)
        self.character = Character(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.character.blitme()
            pygame.display.flip()

if __name__ == "__main__":
    game = TestGame()
    game.run_game()