import unittest
from unittest.mock import patch
from io import StringIO
import main  

class TestGame(unittest.TestCase):
    @patch('builtins.input', side_effect=[50])
    def test_player_turn(self, mock_input):
        secret_number = 50
        self.assertTrue(main.player_turn(secret_number))

    def test_generate_secret_number(self):
        secret_number = main.generate_secret_number()
        self.assertTrue(1 <= secret_number <= 100)

    @patch('random.randint', return_value=50)
    def test_computer_turn(self, mock_randint):
        secret_number = 50
        self.assertTrue(main.computer_turn(secret_number))

class TestPlayerTurn(unittest.TestCase):

    # Caso de prueba para un número válido dentro del rango (50)
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=["50"])
    def test_valid_guess_within_range(self, mock_input, mock_stdout):
        secret_number = 50
        result = main.player_turn(secret_number)
        self.assertTrue(result)
        self.assertIn("¡Felicidades! ¡Has adivinado el número secreto!", mock_stdout.getvalue())

    # Caso de prueba para un número fuera del rango (0)
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=["0", "50"])
    def test_guess_out_of_range_low(self, mock_input, mock_stdout):
        secret_number = 50
        result = main.player_turn(secret_number)
        self.assertFalse(result)
        self.assertIn("Por favor, ingresa un número válido entre 1 y 100.", mock_stdout.getvalue())

    # Caso de prueba para un número fuera del rango (101)
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=["101", "50"])
    def test_guess_out_of_range_high(self, mock_input, mock_stdout):
        secret_number = 50
        result = main.player_turn(secret_number)
        self.assertFalse(result)
        self.assertIn("Por favor, ingresa un número válido entre 1 y 100.", mock_stdout.getvalue())

    # Caso de prueba para una letra ("a")
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=["a", "50"])
    def test_invalid_input_letter(self, mock_input, mock_stdout):
        secret_number = 50
        result = main.player_turn(secret_number)
        self.assertFalse(result)
        self.assertIn("Por favor, ingresa un número válido entre 1 y 100.", mock_stdout.getvalue())

    # Caso de prueba para un símbolo ("$")
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=["$", "50"])
    def test_invalid_input_symbol(self, mock_input, mock_stdout):
        secret_number = 50
        result = main.player_turn(secret_number)
        self.assertFalse(result)
        self.assertIn("Por favor, ingresa un número válido entre 1 y 100.", mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()
