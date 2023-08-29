from game.models import BagTiles

class Player:
    def __init__(self):
        self.score = 0
        self.tiles = []
        self.turn = False

    def getTiles(self, cant, bag = BagTiles):
        if cant  > 0 and cant <= 7:
            for k in range(cant):
                self.tiles.append(bag.take(1))

    def startTurn(self):
        self.turn = True

    def endTurn(self):
        self.turn = False


                
