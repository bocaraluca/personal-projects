import unittest

from domain.computer_strategy import ComputerStrategy, ComputerMediumStrategy, ComputerHardStrategy
from domain.othello_game import OthelloGame


class TestComputerStrategy(unittest.TestCase):
    def setUp(self):
        self.game = OthelloGame('X')
        self.strategy = ComputerStrategy(self.game)

    def test_init(self):
        self.assertEqual(self.strategy._symbol, 'O')
        self.assertEqual(self.strategy._opp_symbol, 'X')

    def test_get_move(self):
        move = self.strategy.get_move(self.game.board, 'O')
        self.assertIn(move, [(2, 4), (3, 5), (4, 2), (5, 3)])

class TestComputerHardStrategy(unittest.TestCase):
    def setUp(self):
        self.game = OthelloGame('X')
        self.strategy = ComputerHardStrategy(self.game)

    def test_get_move(self):
        move = self.strategy.get_move(self.game.board, 'O')
        self.assertIn(move, [(2, 4), (3, 5), (4, 2), (5, 3)])

    def test_is_winning_move(self):
        self.assertFalse(self.strategy.is_winning_move((2, 4)))
        self.assertFalse(self.strategy.is_winning_move((3, 5)))
        self.assertFalse(self.strategy.is_winning_move((4, 2)))
        self.assertFalse(self.strategy.is_winning_move((5, 3)))

    def test_is_corner_move(self):
        self.assertFalse(self.strategy.is_corner_move((2, 4)))
        self.assertTrue(self.strategy.is_corner_move((0, 7)))

    def test_check_win(self):
        self.assertFalse(self.strategy.check_win('O', self.game.board))
        self.assertFalse(self.strategy.check_win('X', self.game.board))

    def test_blocks_opponent_winning_move(self):
        self.assertFalse(self.strategy.blocks_opponent_winning_move((2, 3)))
        self.assertFalse(self.strategy.blocks_opponent_winning_move((3, 2)))
        self.assertFalse(self.strategy.blocks_opponent_winning_move((4, 5)))
        self.assertFalse(self.strategy.blocks_opponent_winning_move((5, 4)))

    def test_get_opp_flips(self):
        self.assertEqual(self.strategy.get_opp_flips((2, 4)), 1)
        self.assertEqual(self.strategy.get_opp_flips((3, 5)), 1)
        self.assertEqual(self.strategy.get_opp_flips((4, 2)), 1)
        self.assertEqual(self.strategy.get_opp_flips((5, 3)), 1)

class TestComputerMediumStrategy(unittest.TestCase):
    def setUp(self):
        self.game = OthelloGame('X')
        self.board = self.game.board
        self.strategy = ComputerMediumStrategy(self.game)

    def test_get_move(self):
        move = self.strategy.get_move(self.game.board, 'O')
        self.assertIn(move, [(2, 4), (3, 5), (4, 2), (5, 3)])

    def test_corner_preference(self):
        self.board.data[0][0] = 'X'
        self.board.data[0][1] = 'O'
        self.board.data[1][0] = 'O'
        self.board.data[1][1] = 'O'
        score = self.strategy.evaluate_board(self.board, 'X')
        self.assertGreater(score, 0)

    def test_minimax_depth(self):
        score_3 = self.strategy.minimax(self.board, 3, True, 'X')
        score_1 = self.strategy.minimax(self.board, 1, True, 'X')
        self.assertGreaterEqual(score_3, score_1)