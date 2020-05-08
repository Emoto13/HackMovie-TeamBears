import unittest

from verification.log_in import verify_user_exists


class TestLogin(unittest.TestCase):
    def test_if_log_in_verification_raises_error_if_no_info_is_given(self):
        err = None

        try:
            verify_user_exists([])
        except Exception as exc:
            err = exc

        self.assertIsNotNone(err)
        self.assertEqual(str(err), 'Wrong user name or password')


if __name__ == '__main__':
    unittest.main()
