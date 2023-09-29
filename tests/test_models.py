import unittest
from game.models import (
    BagTiles,
    Tile,
)
from unittest.mock import patch


class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)

    def test_tile_II(self):
        tile = Tile('B', 2)
        self.assertEqual(tile.letter, 'B')
        self.assertEqual(tile.value, 2)


class TestBagTiles(unittest.TestCase):
    def testPuntajes_I(self):
        values = BagTiles().tiles
        self.assertEqual(values['A'], 1)

    def testPuntajes_II(self):
        values = BagTiles().tiles
        self.assertEqual(values['Z'], 10)

    def testInit(self):
        values = BagTiles()
        values.initialTiles()
        self.assertEqual(values.bagTiles, ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
                   'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E','E', 'E', 'E',
                   'O', 'O','O', 'O','O', 'O',
                   'S', 'S', 'S', 'S','S', 'S',
                   'N', 'N', 'N', 'N', 'N',
                   'R', 'R', 'R', 'R', 'R',
                   'U', 'U', 'U', 'U', 'U',
                   'D', 'D', 'D', 'D', 'D',
                   'L', 'L', 'L', 'L',
                   'T', 'T', 'T', 'T',
                   'C', 'C', 'C', 'C',
                   'G', 'G',
                   'B', 'B',
                   'M', 'M',
                   'P', 'P',
                   'H', 'H',
                   'K',
                   'F',
                   'V',
                   'Y',
                   'J',
                   'LL',
                   'Ñ',
                   'RR',
                   'X',
                   'Z'
                      ])
    # @patch('random.shuffle')
    # def test_bag_tiles(self, patch_shuffle):
    #     bag = BagTiles()
    #     self.assertEqual(
    #         len(bag.tiles),
    #         5,
    #     )
    #     self.assertEqual(
    #         patch_shuffle.call_count,
    #         1,
    #     )
    #     self.assertEqual(
    #         patch_shuffle.call_args[0][0],
    #         bag.tiles,
    #     )


    # def test_take_initial(self):
    #     bag = BagTiles()
    #     initial_tiles = len(bag.tiles)
    #     initial_take_tiles = bag.take(7)
    #     self.assertEqual(
    #         len(initial_take_tiles),
    #         7,
    #     )
    #     self.assertEqual(
    #         len(bag.tiles),
    #         initial_tiles - 7,
    #     )

    # def test_put_I(self):
    #     bag = BagTiles()
    #     currently_tiles = len(bag.tiles)
    #     put_tiles = [Tile('A', 1), Tile('Z', 10), Tile('Y', 4)]
    #     bag.put(put_tiles)
    #     self.assertEqual(
    #         len(bag.tiles),
    #         currently_tiles + 3,
    #     )


if __name__ == '__main__':
    unittest.main()
