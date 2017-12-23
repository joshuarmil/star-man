from game.map.map_square import EmptySquare, PlayerSquare


class Map:
    def __init__(self, size):

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
                if n == 0 and m == 0:
                    map_square = PlayerSquare(
                        self.square_length_in_pixels,
                        horizontal_square_position,
                        vertical_square_position
                    )
                else:
                    map_square = EmptySquare(
                        self.square_length_in_pixels,
                        horizontal_square_position,
                        vertical_square_position
                    )

                map_row.append(map_square)

                horizontal_square_position += self.square_length_in_pixels + self.padding

            game_map.append(map_row)

            vertical_square_position += self.square_length_in_pixels + self.padding

        return game_map
