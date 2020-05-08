import unittest
from utils.decorators.log_in_decorators import already_logged_in


class Factory:
    def __init__(self, is_logged_in=True):
        self.is_logged_in = is_logged_in


class TestLogInDecorators(unittest.TestCase):
    def test_if_already_logged_raises_error_if_logged_in(self):

        @already_logged_in
        def test_func(factory):
            pass

        test_class = Factory()
        err = None

        try:
            test_func(test_class)
        except Exception as exc:
            err = exc

        self.assertIsNotNone(err)
        self.assertEqual(str(err), 'You cannot execute this while logged in')


if __name__ == '__main__':
    unittest.main()
