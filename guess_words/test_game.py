import unittest
from unittest.mock import patch
import builtins
from main import fetch_words_from_api, play_susun_kata

class TestGameFunctions(unittest.TestCase):

    def test_fetch_words_returns_valid_words(self):
        words = fetch_words_from_api(length=5, max_results=5)
        self.assertIsInstance(words, list)
        self.assertGreater(len(words), 0)
        for word in words:
            self.assertTrue(word.isalpha())

    def test_fetch_words_invalid_length(self):
        with self.assertRaises(AssertionError):
            fetch_words_from_api(length=-1)

    @patch('builtins.input', side_effect=['wrongword', 'correct'])
    def test_play_susun_kata_logic(self, mock_input):
        words = ['correct']
        # cheat=True agar tahu jawabannya
        play_susun_kata(words, rounds=1, cheat=True)

if __name__ == '__main__':
    unittest.main()
