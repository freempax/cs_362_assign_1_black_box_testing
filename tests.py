from credit_card_validator import credit_card_validator
import unittest

class TestCreditCardValidator(unittest.TestCase):

    def test_valid_visa(self):
        self.assertTrue(credit_card_validator("4111111111111111"))  # Valid Visa

    def test_valid_mastercard(self):
        self.assertTrue(credit_card_validator("5500000000000004"))  # Valid MasterCard

    def test_valid_amex(self):
        self.assertTrue(credit_card_validator("340000000000009"))  # Valid American Express

    def test_invalid_length_short(self):
        self.assertFalse(credit_card_validator("4111111"))  # Too short

    def test_invalid_length_long(self):
        self.assertFalse(credit_card_validator("41111111111111111111"))  # Too long

    def test_invalid_characters(self):
        self.assertFalse(credit_card_validator("4111-1111-1111-111a"))  # Invalid characters

    def test_invalid_luhn(self):
        self.assertFalse(credit_card_validator("4111111111111121"))  # Fails Luhn check

    def test_empty_string(self):
        self.assertFalse(credit_card_validator(""))  # Empty string

    def test_none_input(self):
        self.assertFalse(credit_card_validator(None))  # None input

if __name__ == '__main__':
    unittest.main()