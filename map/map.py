import pygame


class Map:
    def __init__(self, size, screen):
        self.screen = screen

        self.available_square_color = (142, 142, 142)
        self.padding = 1

        self.square_length_in_pixels = 32

        self.width = self.height = size

        self.height_in_pixels = size * (self.square_length_in_pixels + self.padding) + self.padding
        self.width_in_pixels = self.height_in_pixels

        self.map = self._build_map()

    def _build_map(self):
        vertical_square_position = self.padding

        game_map = []

        for m in range(self.height):
            map_row = []

            horizontal_square_position = self.padding
            for n in range(self.width):
                map_rect = pygame.Rect(
                    horizontal_square_position,
                    vertical_square_position,
                    self.square_length_in_pixels,
                    self.square_length_in_pixels
                )

                map_row.append(map_rect)

                horizontal_square_position += self.square_length_in_pixels + self.padding

            game_map.append(map_row)

            vertical_square_position += self.square_length_in_pixels + self.padding

        return game_map

    def draw_map(self):
        for row in self.map:
            for map_rect in row:

                pygame.draw.rect(
                    self.screen,
                    self.available_square_color,
                    map_rect
                )

