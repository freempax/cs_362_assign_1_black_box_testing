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

    def test_invalid_length_one_digit(self):
        """Testing with a single-digit input (invalid length)."""
        self.assertFalse(credit_card_validator("4"))

    def test_invalid_length_twelve_digits(self):
        """Testing with a 12-digit input (commonly too short)."""
        self.assertFalse(credit_card_validator("123456789012"))

    def test_invalid_length_twenty_digits(self):
        """Testing with a 20-digit input (too long)."""
        self.assertFalse(credit_card_validator("4" * 20))

    def test_visa_valid_alt(self):
        """Visa valid; alt exemplar. Partition: Visa happy path."""
        self.assertTrue(credit_card_validator("4012888888881881"))

    def test_visa_len_15_invalid(self):
        """Visa wrong length 15. BVA around 16."""
        self.assertFalse(credit_card_validator("411111111111111"))

    def test_visa_len_17_invalid(self):
        """Visa wrong length 17. BVA around 16."""
        self.assertFalse(credit_card_validator("40000000000000000"))

    def test_mc_51_lower_edge_valid(self):
        """MC 51 lower bound valid. Partition edge 51–55."""
        self.assertTrue(credit_card_validator("5105105105105100"))

    def test_mc_55_upper_edge_valid(self):
        """MC 55 upper bound valid. Partition edge 51–55."""
        self.assertTrue(credit_card_validator("5555555555554444"))

    def test_mc_51_bad_luhn(self):
        """MC 51 bad Luhn with valid length. Error guessing."""
        self.assertFalse(credit_card_validator("5105105105105101"))

    def test_mc_51_len_15_invalid(self):
        """MC 51 wrong length 15. BVA."""
        self.assertFalse(credit_card_validator("510510510510510"))

    def test_mc_51_len_17_invalid(self):
        """MC 51 wrong length 17. BVA."""
        self.assertFalse(credit_card_validator("51051051051051000"))

    def test_mc_56_invalid_prefix(self):
        """MC near-miss 56 should be rejected. Partition trap."""
        self.assertFalse(credit_card_validator("5610591081018250"))

    def test_mc_2series_valid_mid(self):
        """MC 2-series mid-range valid. Partition."""
        self.assertTrue(credit_card_validator("2223000048400011"))

    def test_mc_2series_lower_bound_valid(self):
        """MC 2221 inclusive lower bound valid. Boundary."""
        # Use a 2221… number with valid Luhn; this one is commonly used:
        self.assertTrue(credit_card_validator("2221000000000009"))

    def test_mc_2series_upper_bound_valid(self):
        """MC 2720 inclusive upper bound valid. Boundary."""
        self.assertTrue(credit_card_validator("2720992718075056"))

    def test_mc_2series_below_range_invalid(self):
        """MC 2220… below lower bound must fail. Off-by-one trap."""
        self.assertFalse(credit_card_validator("2220000000000009"))

    def test_mc_2series_above_range_invalid(self):
        """MC 2721… above upper bound must fail. Off-by-one trap."""
        self.assertFalse(credit_card_validator("2721000000000008"))

    def test_mc_2series_bad_luhn(self):
        """MC 2-series valid prefix/length but bad Luhn should fail."""
        self.assertFalse(credit_card_validator("2223000048400012"))

    def test_amex_37_valid(self):
        """AmEx 37 valid. Partition."""
        self.assertTrue(credit_card_validator("378282246310005"))

    def test_amex_len_16_invalid(self):
        """AmEx wrong length 16 should fail. BVA."""
        self.assertFalse(credit_card_validator("3782822463100050"))

    def test_amex_bad_luhn(self):
        """AmEx valid prefix/length but bad Luhn should fail."""
        self.assertFalse(credit_card_validator("378282246310006"))

    def test_discover_like_6011_rejected(self):
        """Unsupported issuer 6011 should be rejected. Partition."""
        self.assertFalse(credit_card_validator("6011111111111117"))

    def test_all_zeros_rejected(self):
        """All zeros should be rejected. Error guessing."""
        self.assertFalse(credit_card_validator("0000000000000000"))

    def test_visa_13_digit_rejected_by_spec(self):
        """13-digit Visa is out-of-spec here, must be False."""
        self.assertFalse(credit_card_validator("4222222222222"))


if __name__ == "__main__":
    unittest.main()
