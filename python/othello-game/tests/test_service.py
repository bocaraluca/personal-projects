import unittest

from service.othello_service import OthelloService


class TestOthelloService(unittest.TestCase):
    def setUp(self):
        self.service = OthelloService('X', 'medium')

    def test_is_valid_human_move(self):
        self.assertTrue(self.service.is_valid_human_move(2, 3))
        self.assertFalse(self.service.is_valid_human_move(3, 3))

    def test_is_valid_computer_move(self):
        self.assertTrue(self.service.is_valid_computer_move(2, 4))
        self.assertFalse(self.service.is_valid_computer_move(3, 3))

    def test_get_cell_value(self):
        self.assertEqual(self.service.get_cell_value(3, 3), 'O')
        self.assertEqual(self.service.get_cell_value(3, 4), 'X')

    def test_get_human_player(self):
        self.assertEqual(self.service.get_human_player(), 'X')

    def test_get_computer_player(self):
        self.assertEqual(self.service.get_computer_player(), 'O')

    def test_get_score(self):
        self.assertEqual(self.service.get_score(), {'X': 2, 'O': 2})

    def test_get_valid_human_moves(self):
        self.assertEqual(self.service.get_valid_human_moves(), [(2, 3), (3, 2), (4, 5), (5, 4)])

    def test_get_valid_computer_moves(self):
        self.assertEqual(self.service.get_valid_computer_moves(), [(2, 4), (3, 5), (4, 2), (5, 3)])

    def test_play_human_move(self):
        self.service.play_human_move(2, 3)
        self.assertEqual(self.service.get_cell_value(2, 3), 'X')
        self.assertEqual(self.service.get_cell_value(3, 3), 'X')

    def test_play_computer_move(self):
        row, col = self.service.play_computer_move()
        self.assertEqual(self.service.get_cell_value(row, col), 'O')

    def test_is_game_over(self):
        self.assertFalse(self.service.is_game_over())