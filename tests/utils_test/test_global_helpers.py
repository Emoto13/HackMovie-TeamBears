import unittest
from utils.global_helpers import is_command_exit


class TestLogInDecorators(unittest.TestCase):
    def test_if_is_command_exit_returns_false_if_command_is_different_than_exit(self):
        command = 'stay'
        expected = False

        result = is_command_exit(command)

        self.assertEqual(result, expected)

    def test_if_is_command_exit_returns_true_if_command_is__exit(self):
        command = 'exit'
        expected = True

        result = is_command_exit(command)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
