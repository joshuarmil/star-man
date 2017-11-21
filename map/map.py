import pygame


class Map:
    def __init__(self, size, screen):
        self.screen = screen
        self.available_square_color = (142, 142, 142)
        self.padding = 1
        self.square_length_in_pixels = 32

        self.width = self.height = size

        self.pixel_height = size * (self.square_length_in_pixels + self.padding) + self.padding
        self.pixel_width = self.pixel_height

    def draw(self):
        vertical_square_position = self.padding

        for m in range(self.height):
            horizontal_square_position = self.padding
            for n in range(self.width):
                pygame.draw.rect(
                    self.screen,
                    self.available_square_color,
                    pygame.Rect(
                        horizontal_square_position,
                        vertical_square_position,
                        self.square_length_in_pixels,
                        self.square_length_in_pixels
                    )
                )

                horizontal_square_position += self.square_length_in_pixels + self.padding

            vertical_square_position += self.square_length_in_pixels + self.padding

