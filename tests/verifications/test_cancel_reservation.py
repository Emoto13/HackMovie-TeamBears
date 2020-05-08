import unittest

from verification.cancel_reservation import is_reservation_id_valid_or_user_wants_to_go_back


class TestCancelReservation(unittest.TestCase):
    def test_if_is_reservation_id_valid_or_user_wants_to_go_back_goes_back_if_given_command_is_back(self):
        command = 'back'
        reservation_ids = ['1', '2', '3']
        err = None

        try:
            is_reservation_id_valid_or_user_wants_to_go_back(command, reservation_ids)
        except Exception as exc:
            err = exc

        self.assertIsNotNone(err)
        self.assertEqual(str(err), 'You cancelled the command.')

    def test_if_is_reservation_id_valid_or_user_wants_to_go_back_returns_true_if_a_valid_id_is_given(self):
        command = '2'
        reservation_ids = [1, 2, 3]
        expected = True

        result = is_reservation_id_valid_or_user_wants_to_go_back(command, reservation_ids)

        self.assertEqual(result, expected)

    def test_if_is_reservation_id_valid_or_user_wants_to_go_back_returns_false_if_a_non_valid_id_is_given(self):
        command = '4'
        reservation_ids = [1, 2, 3]
        expected = False

        result = is_reservation_id_valid_or_user_wants_to_go_back(command, reservation_ids)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
