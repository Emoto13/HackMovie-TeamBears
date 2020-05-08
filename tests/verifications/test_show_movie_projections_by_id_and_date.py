import unittest

from verification.show_movie_projections_by_id_and_date import verify_projections


class TestShowMovieProjectiosByIdAndDate(unittest.TestCase):
    def test_if_verify_projections_raises_error_if_no_projections_are_found(self):
        err = None

        try:
            verify_projections([])
        except Exception as exc:
            err = exc

        self.assertIsNotNone(err)
        self.assertEqual(str(err), 'No projections for this movie')


if __name__ == '__main__':
    unittest.main()
