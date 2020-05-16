import unittest
from verification.sign_up import is_user_name_unique, is_password_secure


class TestSignUp(unittest.TestCase):
    # TODO fix this test its wrong and dependant on outside conditions

    #    def test_if_verify_user_name_uniqueness_returns_false_if_username_is_taken(self):
    #        user_name = 'Martin Angelov'
    #        expected = False
    #
    #        result = is_user_name_unique(user_name)
    #
    #        self.assertEqual(result, expected)

 #  def test_if_verify_user_name_uniqueness_returns_true_if_username_is_not_taken(self):
 #      user_name = 'Baba Yaga'
 #      expected = True

 #      result = is_user_name_unique(user_name)

 #      self.assertEqual(result, expected)

    def test_if_verify_password_params_returns_false_if_password_length_is_less_than_8(self):
        password = 'asd'
        verification_password = 'asd'
        expected = False

        result = is_password_secure(password, verification_password)

        self.assertEqual(result, expected)

    def test_if_verify_password_params_returns_false_if_passowrd_is_not_same_as_verification_passowrd(self):
        password = 'asdfasdf'
        verification_password = 'asdfasdf2'
        expected = False

        result = is_password_secure(password, verification_password)

        self.assertEqual(result, expected)

    def test_if_verify_password_params_returns_false_if_password_does_not_have_atleast_one_uppercase_letter(self):
        password = 'afgffsdfd!'
        verification_password = 'afgffsdfd!'
        expected = False

        result = is_password_secure(password, verification_password)

        self.assertEqual(result, expected)

    def test_if_verify_password_params_returns_false_if_password_does_not_have_atlest_one_special_char(self):
        password = 'Afgffsdfddsa'
        verification_password = 'Afgffsdfddsa'
        expected = False

        result = is_password_secure(password, verification_password)

        self.assertEqual(result, expected)

    def test_if_verify_password_params_returns_true_if_all_params_are_applied(self):
        password = 'Afgffsdfddsa!'
        verification_password = 'Afgffsdfddsa!'
        expected = True

        result = is_password_secure(password, verification_password)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
