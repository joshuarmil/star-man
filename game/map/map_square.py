import pygame


class MapSquare:

    def __init__(self, length_in_pixels, horizontal_position, vertical_position, color):
        self.color = color
        self.length_in_pixels = length_in_pixels
        self.rect = pygame.Rect(
            horizontal_position,
            vertical_position,
            self.length_in_pixels,
            self.length_in_pixels
        )


class EmptySquare(MapSquare):

    def __init__(self, length_in_pixels, horizontal_position, vertical_position):
        color = (142, 142, 142)
        super().__init__(length_in_pixels, horizontal_position, vertical_position, color)


class PlayerSquare(MapSquare):

    def __init__(self, length_in_pixels, horizontal_position, vertical_position):
        color = (0, 0, 0)
        super().__init__(length_in_pixels, horizontal_position, vertical_position, color)

