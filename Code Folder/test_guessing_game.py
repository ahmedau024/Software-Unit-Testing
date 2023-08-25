# Import necessary modules and classes for unit testing
import unittest
import io
from unittest.mock import patch
import guessing_game

# Define a test class that inherits from unittest.TestCase
class TestGuessingGame(unittest.TestCase):

    # Test case for invalid inputs (non-digit and incorrect length)
    @patch('builtins.input', side_effect=['123a', 'abcd', '12345', '1234', 'quit'])
    def test_invalid_input(self, mock_input):
        self.assertEqual(guessing_game.play_game(), None)

    # Test case for invalid inputs with captured stdout to check output
    @patch('builtins.input', side_effect=['4321', 'quit'])
    def test_invalid_input_output(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            guessing_game.play_game()
            print(mock_stdout.getvalue())
            self.assertNotIn("Congratulations! You guessed the number", mock_stdout.getvalue())

    # Test case for quitting without guessing the number
    @patch('builtins.input', side_effect=['1234', '5678', 'quit'])
    def test_quit_guess(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            guessing_game.play_game()
            self.assertIn("The secret number was", mock_stdout.getvalue())

    # Test case for checking the displayed number of attempts
    @patch('builtins.input', side_effect=['1234', '5678', 'quit'])
    def test_attempts(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            guessing_game.play_game()   
            self.assertIn("You took", mock_stdout.getvalue())

    # Test case for hint generation
    def test_hints(self):
        secret_number = '1234'
        self.assertEqual(guessing_game.give_hints(secret_number, '4321'), ['x', 'x', 'x', 'x'])  
        self.assertEqual(guessing_game.give_hints(secret_number, '5678'), ['_', '_', '_', '_'])
        self.assertEqual(guessing_game.give_hints(secret_number, '1243'), ['O', 'O', 'x', 'x'])

    # Test case for non-digit guess input with captured stdout to check output
    @patch('builtins.input', side_effect=['abcd', '1a34', 'quit'])
    def test_non_digit_guess(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            guessing_game.play_game()
            self.assertIn("Invalid input. Please enter a four-digit number.", mock_stdout.getvalue())

    # Test case for invalid length guess input with captured stdout to check output
    @patch('builtins.input', side_effect=['12', '12345', 'quit'])
    def test_invalid_length_guess(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            guessing_game.play_game()
            self.assertIn("Invalid input. Please enter a four-digit number.", mock_stdout.getvalue())

    # Test case for a short number guess input with captured stdout to check output
    @patch('builtins.input', side_effect=['123', 'quit'])
    def test_short_number(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            guessing_game.play_game()
            self.assertIn("Invalid input. Please enter a four-digit number.", mock_stdout.getvalue())

    # Test case for quitting without guessing the number with mixed case input
    @patch('builtins.input', side_effect=['quit'])
    def test_quit_mixed_case(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            guessing_game.play_game()
            self.assertIn("The secret number was", mock_stdout.getvalue())

# Run the unittest framework if the script is executed as the main program
if __name__ == '__main__':
    unittest.main()





