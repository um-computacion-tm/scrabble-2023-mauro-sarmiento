import random

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value


class BagTiles:
    def __init__(self):
        self.tiles = {'A': 1,
                     'E': 1,
                     'O': 1,
                     'I': 1,
                     'S': 1,
                     'N': 1,
                     'L': 1,
                     'R': 1,
                     'U': 1,
                     'T': 1,
                     'D': 2,
                     'G': 2,
                     'C': 3,
                     'B': 3,
                     'M': 3,
                     'K': 3,
                     'P': 3,
                     'H': 4,
                     'F': 4,
                     'V': 4,
                     'Y': 4,
                     'CH': 5,
                     'Q': 5,
                     'J': 8,
                     'LL': 8,
                     'Ñ': 8,
                     'RR': 8,
                     'X': 8,
                     'Z': 10,
                     'CO': 0
        }
        # random.shuffle(self.tiles)

    # def initialTiles(self):
    #     initial = {
    #         ''
    #     }

    # def take(self, count):
    #     tiles = []
    #     for _ in range(count):
    #         tiles.append(self.tiles.pop())
    #     return tiles

    # def put(self, tiles):
    #     self.tiles.extend(tiles)


    
