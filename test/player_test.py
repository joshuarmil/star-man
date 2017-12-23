import unittest

from game.map.map_square import PlayerSquare

from game.map.map import Map


class PlayerAcceptanceTest(unittest.TestCase):

    def test_player_exists(self):
        game_map = Map(14)

        flattened_game_matrix = [game_square for row in game_map.map for game_square in row]

        if any(isinstance(game_square, PlayerSquare) for game_square in flattened_game_matrix):
            return True
        else:
            return False


if __name__ == "__main__":
    unittest.main()
