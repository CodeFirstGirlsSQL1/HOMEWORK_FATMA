from unittest import mock
from unittest import TestCase, main
from ATM_program import verify_pin, log_in, run_atm


class TestVerifyPinFunction(TestCase):

    def test_correct_pin(self):
        expected = True
        result = verify_pin(pin='1234')
        self.assertEqual(expected, result)

    def test_incorrect_pin(self):
        expected = False
        result = verify_pin(pin='0987')
        self.assertEqual(expected, result)

    def test_invalid_input(self):
        expected = False
        result = verify_pin(1234)
        self.assertEqual(expected, result)

    def test_wrong_input_length(self):
        expected = False
        result = verify_pin("123456")
        self.assertEqual(expected, result)


class TestLogInFunction(TestCase):

    @mock.patch('ATM_program.input')
    def test_correct_login(self, mock_input):
        with mock.patch('builtins.input'):
            mock_input.return_value = "1234"
            expected = True
            self.assertEqual(expected, log_in())

    @mock.patch('ATM_program.input')
    def test_incorrect_login(self, mock_input):
        with mock.patch('builtins.input'):
            mock_input.return_value = "0987"
            expected = False
            self.assertEqual(expected, log_in())


class TestRunATMFunction(TestCase):

    # test a successful withdrawal
    @mock.patch('ATM_program.input')
    def test_successful_withdrawal(self, mock_input):
        with mock.patch('builtins.input'):
            mock_input.return_value = "1234"
            expected = 75
            self.assertEqual(expected, run_atm(25))

    # test a an unsuccessful login
    @mock.patch('ATM_program.input')
    def test_unsuccessful_login(self, mock_input):
        with mock.patch('builtins.input'):
            mock_input.return_value = "0000"
            expected = None
            actual = run_atm(25)
            self.assertEqual(expected, actual)

    # test a successful login but insufficient funds
    @mock.patch('ATM_program.input')
    def test_not_enough_funds_in_account(self, mock_input):
        with mock.patch('builtins.input'):
            with self.assertRaises(ValueError):
                mock_input.return_value = "1234"
                expected = ValueError
                self.assertEqual(expected, run_atm(125))

if __name__ == "__main__":
    main()