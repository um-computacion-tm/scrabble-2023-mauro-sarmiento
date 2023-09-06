import unittest
from game.board import Board


class TestBoard(unittest.TestCase):
    def test_init(self):
        tablero = Board()
        self.assertEqual((tablero.board),[])

    def testTableroInicial(self):
        tablero = Board()
        tablero.initialBoard()
        self.assertEqual((tablero.board),[
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
])
    
    def testTableroConPalabrasGrafico(self):
        tablero = Board()
        tablero.initialBoard()
        tablero.board[0][0] = 'A'
        tablero.board[1][0] = 'R'
        tablero.board[2][0] = 'A'
        tablero.board[3][0] = 'S'
        tablero.board[4][0] = 'A'
        tablero.board[5][0] = 'K'
        tablero.board[6][0] = 'A'
        self.assertEqual((tablero.board),[
    ['A','*','*','4','*','*','*','0','*','*','*','4','*','*','0'],
    ['R','1','*','*','*','5','*','*','*','5','*','*','*','1','*'],
    ['A','*','1','*','*','*','4','*','4','*','*','*','1','*','*'],
    ['S','*','*','1','*','*','*','4','*','*','*','1','*','*','*'],
    ['A','*','*','*','1','*','*','*','*','*','1','*','*','*','4'],
    ['K','5','*','*','*','5','*','*','*','5','*','*','*','5','*'],
    ['A','*','4','*','*','*','4','*','4','*','*','*','4','*','*'],
    ['0','*','*','4','*','*','*','1','*','*','*','4','*','*','0'],
    ['*','*','4','*','*','*','4','*','4','*','*','*','4','*','*'],
    ['*','5','*','*','*','5','*','*','*','5','*','*','*','5','*'],
    ['*','*','*','*','1','*','*','*','*','*','1','*','*','*','*'],
    ['4','*','*','1','*','*','*','4','*','*','*','1','*','*','4'],
    ['*','*','1','*','*','*','4','*','4','*','*','*','1','*','*'],
    ['*','1','*','*','*','5','*','*','*','5','*','*','*','1','*'],
    ['0','*','*','4','*','*','*','0','*','*','*','4','*','*','0'],
])
                
    def testValidarEnVertical(self):
        tablero = Board()
        tablero.initialBoard()
        tablero.board[0][0] = 'A'
        tablero.board[1][0] = 'R'
        tablero.board[2][0] = 'A'
        tablero.board[3][0] = 'S'
        tablero.board[4][0] = 'A'
        tablero.board[5][0] = 'K'
        tablero.board[6][0] = 'A'
        self.assertEqual((tablero.verticalWord('ARASAKA')), True)

    def testValidarEnVerticalFalso(self):
        tablero = Board()
        tablero.initialBoard()
        tablero.board[0][0] = 'A'
        tablero.board[1][0] = 'R'
        tablero.board[2][0] = 'A'
        tablero.board[3][0] = 'S'
        tablero.board[4][0] = 'A'
        tablero.board[5][0] = 'K'
        tablero.board[6][0] = 'A'
        self.assertEqual((tablero.verticalWord('CASA')), None)

    def testValidarEnHorizontal(self):
        tablero = Board()
        tablero.initialBoard()
        tablero.board[3][3] = 'A'
        tablero.board[3][4] = 'R'
        tablero.board[3][5] = 'A'
        tablero.board[3][6] = 'S'
        tablero.board[3][7] = 'A'
        tablero.board[3][8] = 'K'
        tablero.board[3][9] = 'A'
        self.assertEqual((tablero.horizontalWord('ARASAKA')), True)

    def testValidarEnHorizontalFalso(self):
        tablero = Board()
        tablero.initialBoard()
        tablero.board[3][3] = 'A'
        tablero.board[3][4] = 'R'
        tablero.board[3][5] = 'A'
        tablero.board[3][6] = 'S'
        tablero.board[3][7] = 'A'
        tablero.board[3][8] = 'K'
        tablero.board[3][9] = 'A'
        self.assertEqual((tablero.horizontalWord('AROSAKO')), None)


    



if __name__ == '__main__':
    unittest.main()
