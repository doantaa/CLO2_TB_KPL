import unittest
from tic_tac_toe_main import check_win, check_draw

class TestTicTacToe(unittest.TestCase):

    def test_check_win_horizontal(self):
        board = ['X', 'X', 'X', '4', '5', '6', '7', '8', '9']
        self.assertTrue(check_win(board, 'X'))

    def test_check_win_vertical(self):
        board = ['X', '2', '3', 'X', '5', '6', 'X', '8', '9']
        self.assertTrue(check_win(board, 'X'))

    def test_check_win_diagonal(self):
        board = ['X', '2', '3', '4', 'X', '6', '7', '8', 'X']
        self.assertTrue(check_win(board, 'X'))

    def test_check_no_win(self):
        board = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
        self.assertFalse(check_win(board, 'X'))

    def test_check_draw_true(self):
        board = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
        self.assertTrue(check_draw(board))

    def test_check_draw_false(self):
        board = ['X', '2', '3', 'X', 'O', '6', '7', 'O', 'X']
        self.assertFalse(check_draw(board))

if __name__ == '__main__':
    unittest.main()
