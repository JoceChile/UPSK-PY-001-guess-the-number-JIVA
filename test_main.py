import unittest
from unittest.mock import patch
import game

class TestGameFunctions(unittest.TestCase):
    @patch('builtins.input', return_value=50)
    def test_generate_secret_number(self, mock_input):
        secret_number = game.generate_secret_number()
        self.assertTrue(1 <= secret_number <= 100)

    @patch('builtins.input', return_value=50)
    def test_get_player_guess(self, mock_input):
        guess = game.get_player_guess()
        self.assertEqual(guess, 50)

    @patch('builtins.input', side_effect=['50'])
    def test_player_turn_correct_guess(self, mock_input):
        with patch('game.get_player_guess', return_value=50):
            self.assertTrue(game.player_turn(50, "Test"))

    @patch('builtins.input', side_effect=['30', '60', '50'])
    def test_player_turn_incorrect_guess(self, mock_input):
        with patch('game.get_player_guess', side_effect=[30, 60, 50]):
            self.assertTrue(game.player_turn(50, "Test"))

    @patch('game.get_computer_guess', return_value=50)
    def test_computer_turn_correct_guess(self, mock_guess):
        self.assertTrue(game.computer_turn(50))

    @patch('game.get_computer_guess', return_value=30)
    def test_computer_turn_incorrect_guess(self, mock_guess):
        self.assertFalse(game.computer_turn(50))

if __name__ == '__main__':
    unittest.main()

