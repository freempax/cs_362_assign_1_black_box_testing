
"""This file calculates if a credit card number is valid using unit tests."""


from credit_card_validator import credit_card_validator
import unittest


class TestCreditCardValidator(unittest.TestCase):
    """Unit tests for credit_card_validator function."""

    def test_valid_visa(self):
        """Testing if input is a valid Visa card number."""
        self.assertTrue(credit_card_validator("4111111111111111"))

    def test_valid_mastercard(self):
        """Testing if input is a valid MasterCard number."""
        self.assertTrue(credit_card_validator("5500000000000004"))

    def test_valid_amex(self):
        """Testing if input is a valid American Express card number."""
        self.assertTrue(credit_card_validator("340000000000009"))

    def test_invalid_length_short(self):
        """Testing if input length is too short."""
        self.assertFalse(credit_card_validator("4111111"))

    def test_invalid_length_long(self):
        """Testing if input length is too long."""
        self.assertFalse(credit_card_validator("41111111111111111111"))

    def test_invalid_luhn(self):
        """Testing if input fails Luhn check."""
        self.assertFalse(credit_card_validator("4111111111111121"))

    def test_empty_string(self):
        """Testing if input is an empty string."""
        self.assertFalse(credit_card_validator(""))

    def test_none_input(self):
        """Testing if input is empty or None."""
        self.assertFalse(credit_card_validator(None))


if __name__ == '__main__':
    unittest.main()
