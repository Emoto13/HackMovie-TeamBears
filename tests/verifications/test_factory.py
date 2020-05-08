import unittest

from verification.factory import verify_command_exists, verify_command_requiring_log_in


class TestFactory(unittest.TestCase):
    def test_verify_command_exists_raises_error_if_given_invalid_command(self):
        command = 'accept'
        commands = {'show': 1, 'decline': 2}
        err = None

        try:
            verify_command_exists(command, commands)
        except Exception as exc:
            err = exc

        self.assertIsNotNone(err)
        self.assertEqual(str(err), "No such command! Try again.")

    def test_verify_command_requiring_log_in_raises_error_if_given_user_is_not_logged_in(self):
        command = 'show_reservations'
        user_is_logged_in = False
        err = None

        try:
            verify_command_requiring_log_in(command, user_is_logged_in)
        except Exception as exc:
            err = exc

        self.assertIsNotNone(err)
        self.assertEqual(str(err), "Please log in to use this command.")


if __name__ == '__main__':
    unittest.main()
