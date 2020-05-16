import unittest
from verification.make_reservation import verify_projections_with_empty_seats_exist, is_ticket_number_valid, \
    is_movie_id_valid, is_projection_id_valid, verify_seat_input, verify_seat_is_in_saloon,\
    verify_seat_is_available, is_action_valid, seat_is_valid

TEMP_SALOON = [
    [' ', '  1', '  2', '  3', '  4', '  5', '  6', '  7', '  8', '  9', '  10'],
    ['1', '  .', '  .', '  .', '  .', '  .', '  .', '  .', '  .', '  .', '  .'],
    ['2', '  .', '  .', '  .', '  .', '  .', '  .', '  .', '  .', '  .', '  .'],
    ['3', '  .', '  .', '  .', '  .', '  .', '  .', '  .', '  .', '  .', '  .'],
    ['4', '  .', '  .', '  .', '  X', '  .', '  .', '  .', '  .', '  .', '  .'],
    ['5', '  .', '  .', '  .', '  .', '  .', '  .', '  .', '  .', '  .', '  .'],
    ['6', '  .', '  .', '  .', '  .', '  .', '  .', '  .', '  .', '  .', '  .'],
    ['7', '  .', '  .', '  .', '  .', '  .', '  .', '  .', '  .', '  .', '  .'],
    ['8', '  .', '  .', '  .', '  .', '  .', '  .', '  .', '  .', '  .', '  .'],
    ['9', '  .', '  .', '  .', '  .', '  .', '  .', '  .', '  .', '  .', '  .'],
    ['10', ' .', '  .', '  .', '  .', '  .', '  .', '  .', '  .', '  .', '  .']
]


class TestMakeReservation(unittest.TestCase):
    def test_if_verify_projections_with_empty_seats_exist_raises_error_if_no_projections_are_given(self):
        projections = []
        err = None

        try:
            verify_projections_with_empty_seats_exist(projections)
        except Exception as exc:
            err = exc

        self.assertIsNotNone(err)
        self.assertEqual(str(err), "Sorry no projections with empty seats found. :'( ")

    def test_if_is_ticket_number_valid_returns_false_if_zero_or_negative_tickets_are_given(self):
        tickets = 0
        expected = False

        result = is_ticket_number_valid(tickets)

        self.assertEqual(result, expected)

    def test_if_is_ticket_number_valid_returns_true_if_postive_number_of_tickets_are_given(self):
        tickets = 5
        expected = True

        result = is_ticket_number_valid(tickets)

        self.assertEqual(result, expected)

    def test_if_is_movie_id_valid_returns_false_if_given_movie_id_is_not_in_movies_id(self):
        movie_id = 5
        movies_id = [1, 2, 3, 4]
        expected = False

        result = is_movie_id_valid(movie_id, movies_id)

        self.assertEqual(result, expected)

    def test_if_is_movie_id_valid_returns_true_if_given_movie_id_is_in_movies_id(self):
        movie_id = 3
        movies_id = [1, 2, 3, 4]
        expected = True

        result = is_movie_id_valid(movie_id, movies_id)

        self.assertEqual(result, expected)

    def test_if_is_projection_id_valid_returns_false_if_projection_id_is_not_in_projections_id(self):
        projection_id = 5
        projections_id = [1, 2, 3, 4]
        expected = False

        result = is_projection_id_valid(projection_id, projections_id)

        self.assertEqual(result, expected)

    def test_if_is_projection_id_valid_returns_true_if_projection_id_is_in_projections_id(self):
        projection_id = 3
        projections_id = [1, 2, 3, 4]
        expected = True

        result = is_projection_id_valid(projection_id, projections_id)

        self.assertEqual(result, expected)

    def test_if_verify_seat_input_returns_false_if_regex_gives_None(self):
        row_and_column = None
        expected = False

        result = verify_seat_input(row_and_column)

        self.assertEqual(result, expected)

    def test_if_verify_seat_input_returns_true_if_regex_gives_seats(self):
        row_and_column = '1,2'
        expected = True

        result = verify_seat_input(row_and_column)

        self.assertEqual(result, expected)

    def test_if_verify_seat_is_in_saloon_returns_false_if_seat_is_not_in_saloon(self):
        row = 15
        col = 20
        saloon = TEMP_SALOON
        expected = False

        result = verify_seat_is_in_saloon(row, col, saloon)

        self.assertEqual(result, expected)

    def test_if_verify_seat_is_in_saloon_returns_true_if_seat_is_in_saloon(self):
        row = 5
        col = 4
        saloon = TEMP_SALOON
        expected = True

        result = verify_seat_is_in_saloon(row, col, saloon)

        self.assertEqual(result, expected)

    def test_if_verify_seat_is_available_returns_false_if_seat_is_taken(self):
        row = 4
        col = 4
        saloon = TEMP_SALOON
        expected = False

        result = verify_seat_is_available(row, col, saloon)

        self.assertEqual(result, expected)

    def test_if_verify_seat_is_available_returns_true_if_seat_is_free(self):
        row = 5
        col = 4
        saloon = TEMP_SALOON
        expected = True

        result = verify_seat_is_available(row, col, saloon)

        self.assertEqual(result, expected)

    def test_if_is_action_valid_returns_false_if_action_is_not_in_actions(self):
        action = 'ahem'
        actions = {'back': 1, 'finalize': 2}
        expected = False

        result = is_action_valid(action, actions)

        self.assertEqual(result, expected)

    def test_if_is_action_valid_returns_true_if_action_is_in_actions(self):
        action = 'finalize'
        actions = {'back': 1, 'finalize': 2}
        expected = True

        result = is_action_valid(action, actions)

        self.assertEqual(result, expected)

    def test_if_seat_is_valid_returns_false_if_seat_is_already_picked_in_current_session(self):
        seat = '5,4'
        saloon = TEMP_SALOON
        seats = [(5, 4)]
        expected = False

        result = seat_is_valid(seat, saloon, seats)

        self.assertEqual(result, expected)

    def test_if_seat_is_valid_returns_true_if_seat_has_not_been_picked_in_current_session(self):
        seat = '5,4'
        saloon = TEMP_SALOON
        seats = []
        expected = True

        result = seat_is_valid(seat, saloon, seats)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
