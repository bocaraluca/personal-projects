import unittest

from domain.othello_board import OthelloBoard


class TestOthelloBoard(unittest.TestCase):
    def setUp(self):
        self.board = OthelloBoard()

    def test_init(self):
        self.assertEqual(self.board.data[3][3], 'O')
        self.assertEqual(self.board.data[3][4], 'X')
        self.assertEqual(self.board.data[4][3], 'X')
        self.assertEqual(self.board.data[4][4], 'O')

    def test_is_valid_move(self):
        self.assertTrue(self.board.is_valid_move(2, 3, 'X'))
        self.assertFalse(self.board.is_valid_move(2, 3, 'O'))

    def test_make_move(self):
        self.board.make_move(2, 3, 'X')
        self.assertEqual(self.board.data[2][3], 'X')
        self.board.make_move(2, 4, 'O')
        self.assertEqual(self.board.data[2][4], 'O')

    def test_get_cell_value(self):
        self.assertEqual(self.board.get_cell_value(3, 3), 'O')
        self.assertEqual(self.board.get_cell_value(3, 4), 'X')

    def test_flip_pieces(self):
        self.board.flip_pieces(2, 3, 'X')
        self.assertEqual(self.board.data[3][3], 'X') # [3, 3] is flipped (between [2, 3] and [4, 3])