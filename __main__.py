import pygame
from map.map import Map

height = 600
width = 400


def run_game():
    try:
        pygame.init()

        screen = pygame.display.set_mode((height, width))

        screen.fill((42, 42, 42))

        game_map = Map(size=14, screen=screen)

        game_map.draw()

        pygame.display.update()

    finally:
        pygame.quit()


if __name__ == "__main__":
    run_game()