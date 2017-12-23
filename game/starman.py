import pygame

from pygame.locals import QUIT

from game.map.map import Map


class StarMan:

    def __init__(self):
        self.height = 600
        self.width = 400

        pygame.init()

        self.screen = pygame.display.set_mode((self.height, self.width))

        self.screen.fill((42, 42, 42))

        self.game_map = Map(size=14)

    def run_game(self):
        try:
            self.draw_map()

            game_running = True

            while game_running:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        game_running = False
                        break

        finally:
            pygame.quit()

    def draw_map(self):
        for row in self.game_map.map:
            for map_square in row:

                pygame.draw.rect(
                    self.screen,
                    map_square.color,
                    map_square.rect
                )
