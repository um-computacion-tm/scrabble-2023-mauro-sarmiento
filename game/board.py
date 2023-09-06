from game.cell import Cell


class Board:
    def __init__(self):
        self.board = []

    def initialBoard(self):
        initialBoard = [
    ['0','*','*','4','*','*','*','0','*','*','*','4','*','*','0'],
    ['*','1','*','*','*','5','*','*','*','5','*','*','*','1','*'],
    ['*','*','1','*','*','*','4','*','4','*','*','*','1','*','*'],
    ['4','*','*','1','*','*','*','4','*','*','*','1','*','*','*'],
    ['*','*','*','*','1','*','*','*','*','*','1','*','*','*','4'],
    ['*','5','*','*','*','5','*','*','*','5','*','*','*','5','*'],
    ['*','*','4','*','*','*','4','*','4','*','*','*','4','*','*'],
    ['0','*','*','4','*','*','*','1','*','*','*','4','*','*','0'],
    ['*','*','4','*','*','*','4','*','4','*','*','*','4','*','*'],
    ['*','5','*','*','*','5','*','*','*','5','*','*','*','5','*'],
    ['*','*','*','*','1','*','*','*','*','*','1','*','*','*','*'],
    ['4','*','*','1','*','*','*','4','*','*','*','1','*','*','4'],
    ['*','*','1','*','*','*','4','*','4','*','*','*','1','*','*'],
    ['*','1','*','*','*','5','*','*','*','5','*','*','*','1','*'],
    ['0','*','*','4','*','*','*','0','*','*','*','4','*','*','0'],
]
        self.board = initialBoard

    def mostrarTableroActual(self):
        for fila in self.board:
            print(fila)

    def verticalWord(self, palabra):
        for k in range(15):
            columna_to_string = ''.join(fila[k] for fila in self.board)
            index = columna_to_string.find(palabra)
            if index != -1:
                return True
            else:
                continue

    def horizontalWord(self, palabra):
        for j in range(15):
            row_to_string = ''.join(str(elemento) for elemento in self.board[j])
            index = row_to_string.find(palabra)
            if index != -1:
                return True
            else:
                continue

