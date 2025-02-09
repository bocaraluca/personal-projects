import unittest

from domain.computer_strategy import ComputerStrategy
from domain.othello_game import OthelloGame


class TestOthelloGame(unittest.TestCase):
    def setUp(self):
        self.game = OthelloGame('X') # human player is 'X'
        self.game.set_computer_strategy(ComputerStrategy(self.game))

    def test_init(self):
        self.assertEqual(self.game.human_player, 'X')
        self.assertEqual(self.game.computer_player, 'O')

    def test_get_valid_moves(self):
        self.assertEqual(self.game.get_valid_moves('X'), [(2, 3), (3, 2), (4, 5), (5, 4)])
        self.assertEqual(self.game.get_valid_moves('O'), [(2, 4), (3, 5), (4, 2), (5, 3)])

    def test_is_valid_move(self):
        self.assertTrue(self.game.is_valid_move(2, 3, 'X'))
        self.assertFalse(self.game.is_valid_move(2, 3, 'O'))

    def test_get_cell_value(self):
        self.assertEqual(self.game.get_cell_value(3, 3), 'O')
        self.assertEqual(self.game.get_cell_value(3, 4), 'X')

    def test_is_game_over(self):
        self.assertFalse(self.game.is_game_over())

    def test_play_human_move(self):
        self.game.play_human_move(2, 3)
        self.assertEqual(self.game.get_cell_value(3, 3), 'X')
        self.assertEqual(self.game.get_cell_value(4, 3), 'X')

    def test_play_computer_move(self):
        row, col = self.game.play_computer_move()
        self.assertEqual(self.game.get_cell_value(row, col), 'O')

    def test_get_score(self):
        self.assertEqual(self.game.get_score(), {'X': 2, 'O': 2})