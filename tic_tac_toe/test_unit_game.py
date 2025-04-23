import unittest
from tic_tac_toe_main import check_win, check_draw  # <-- ini penting

class TestTicTacToeFunctions(unittest.TestCase):
    def test_check_win(self):
        board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertTrue(check_win(board, 'X'))
        self.assertFalse(check_win(board, 'O'))

    def test_check_draw(self):
        board = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
        self.assertTrue(check_draw(board))

if __name__ == "__main__":
    unittest.main()
