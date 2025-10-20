# Paxton Freeman
# CS 362 - Software Engineering
# Assignment 1 - Black Box Testing
# 10-20-2025
# """This file calculates if a credit card number is valid using unit tests."""

from credit_card_validator import credit_card_validator
import unittest


class TestCreditCardValidator(unittest.TestCase):
    """Unit tests for credit_card_validator function."""

    # Visa
    def test_1(self):
        """
        Testing if input is a valid Visa card number.
        Boundary Value Testing
        """
        self.assertTrue(credit_card_validator("4111111111111111"))

    # MasterCard
    def test_2(self):
        """
        Testing if input is a valid MasterCard number.
        Boundary Value Testing
        """
        self.assertTrue(credit_card_validator("5500000000000004"))

    # American Express
    def test_3(self):
        """
        Testing if input is a valid American Express card number
        Boundary Value Testing
        """
        self.assertTrue(credit_card_validator("340000000000009"))

    # General Tests
    def test_4(self):
        """
        Testing if input length is too short
        Boundary Value Testing
        """
        self.assertFalse(credit_card_validator("4111111"))

    def test_5(self):
        """
        Testing if input length is too long
        Boundary Value Testing
        """
        self.assertFalse(credit_card_validator("41111111111111111111"))

    def test_6(self):
        """
        Testing if input fails Luhn check
        Error Guessing
        """
        self.assertFalse(credit_card_validator("4111111111111121"))

    def test_7(self):
        """
        Testing if input is an empty string
        Error Guessing
        """
        self.assertFalse(credit_card_validator(""))

    def test_8(self):
        """
        Testing if input is empty or None
        Error Guessing
        """
        self.assertFalse(credit_card_validator(None))

    def test_9(self):
        """
        Testing with a single-digit input (invalid length).
        Error Guessing
        """
        self.assertFalse(credit_card_validator("4"))

    def test_11(self):
        """
        Testing with a 20-digit input
        Error Guessing
        """
        self.assertFalse(credit_card_validator("4" * 20))

    def test_12(self):
        """
        Visa Valid input
        Partition Testing.
        """
        self.assertTrue(credit_card_validator("4012888888881881"))

    def test_13(self):
        """
        Visa Invalid input
        Partition Testing.
        """
        self.assertFalse(credit_card_validator("411111111111111"))

    def test_14(self):
        """
        Visa Invalid input
        Partition Testing.
        """
        self.assertFalse(credit_card_validator("40000000000000000"))

    def test_15(self):
        """
        MC Valid input
        Partition Testing.
        """
        self.assertTrue(credit_card_validator("5105105105105100"))

    def test_16(self):
        """
        MC Valid input
        Partition Testing.
        """
        self.assertTrue(credit_card_validator("5555555555554444"))

    def test_17(self):
        """
        MC Bad Luhn
        Error guessing.
        """
        self.assertFalse(credit_card_validator("5105105105105101"))

    def test_18(self):
        """
        MC wrong Length
        Boundary Testing
        """
        self.assertFalse(credit_card_validator("510510510510510"))

    def test_19(self):
        """
        MC wrong length
        Boundary Testing
        """
        self.assertFalse(credit_card_validator("51051051051051000"))

    def test_20(self):
        """
        MC with 17 Characters with invalid prefix
        Boundary Testing
        """
        self.assertFalse(credit_card_validator("5610591081018250"))

    def test_21(self):
        """
        MC testing valid prefix
        Partition Testing."""
        self.assertTrue(credit_card_validator("2223000048400011"))

    def test_22(self):
        """MC testing with bad luhn"""
        """Error guessing."""
        self.assertTrue(credit_card_validator("2221000000000009"))

    def test_23(self):
        """MC top of boundary"""
        """Boundary Testing."""
        self.assertTrue(credit_card_validator("2720992718075056"))

    def test_24(self):
        """
        MC below boundary
        Boundary Testing.
        """
        self.assertFalse(credit_card_validator("2220000000000009"))

    def test_25(self):
        """
        MC Above boundary
        Boundary Testing.
        """
        self.assertFalse(credit_card_validator("2721000000000008"))

    def test_26(self):
        """
        MC bad Luhn
        Error guessing.
        """
        self.assertFalse(credit_card_validator("2223000048400012"))

    def test_27(self):
        """
        AMEX Top of boundary
        Boundary Testing.
        """
        self.assertTrue(credit_card_validator("378282246310005"))

    def test_28(self):
        """
        AMEX Incorrect length
        Boundary Testing.
        """
        self.assertFalse(credit_card_validator("3782822463100050"))

    def test_29(self):
        """
        AMEX valid prefix/length but bad Luhn.
        Error guessing.
        """
        self.assertFalse(credit_card_validator("378282246310006"))

    def test_31(self):
        """
        All zeros
        Error guessing.
        """
        self.assertFalse(credit_card_validator("0000000000000000"))

    def test_32(self):
        """
        Visa - 13-digit
        Error Guesssing.
        """
        self.assertFalse(credit_card_validator("4222222222222"))

    def test_33(self):
        """
        MC Below Boundary
        Boundary Testing.
        """
        self.assertFalse(credit_card_validator("5012345678901234"))

    def test_35(self):
        """
        AMEX Below boundary
        Partition testing.
        """
        self.assertFalse(credit_card_validator("361111111111111"))

    def test_36(self):
        """
        AMEX Below boundary
        Partition testing.
        """
        self.assertFalse(credit_card_validator("381111111111111"))

    def test_37(self):
        """
        MC wrong Length 15
        Error guessing.
        """
        self.assertFalse(credit_card_validator("222100000000000"))

    def test_38(self):
        """
        MC Wrong Boundary and Length
        Boundary Testing.
        """
        self.assertFalse(credit_card_validator("27200000000000000"))

    def test_39(self):
        """
        Different card input.
        Error guessing.
        """
        self.assertFalse(credit_card_validator("6011111111111117"))

    def test_41(self):
        """
        Luhn-bad
        Error guessing.
        """
        self.assertFalse(credit_card_validator("2720992718075057"))

    def test_42(self):
        """
        MC Valid Partition
        Partition Testing.
        """
        self.assertTrue(credit_card_validator("5200828282828210"))

    def test_43(self):
        """
        MC 53 valid Partition
        Partition Testing.
        """
        self.assertTrue(credit_card_validator("5301250070000191"))

    def test_44(self):
        """
        MC 53 valid Partition
        Partition Testing."""
        self.assertTrue(credit_card_validator("5454545454545454"))

    def test_45(self):
        """
        AMEX 53 valid Partition
        Partition Testing.
        """
        self.assertFalse(credit_card_validator("361111111111111"))

    def test_47(self):
        """
        MC 53 valid Partition
        Partition Testing.
        """
        self.assertTrue(credit_card_validator("2221000000000009"))

    def test_48(self):
        """
        MC 53 valid Partition
        Partition Testing.
        """
        self.assertTrue(credit_card_validator("2720992718075056"))

    def test_49(self):
        """
        Visa prefix 4 but 19 digits.
        Boundary Value Analysis around 16.
        """
        self.assertFalse(credit_card_validator("4000000000000000008"))

    def test_50(self):
        """
        Visa prefix 4 but with 10 digits.
        Boundary Value Analysis around 16."""
        self.assertFalse(credit_card_validator("4111111111"))

    def test_51(self):
        """
        AMEX 34 but with 14 digits.
        Boundary Value Analysis."""
        self.assertFalse(credit_card_validator("34000000000000"))

    def test_52(self):
        """
        MC but with 14 digits.
        Boundary Value Analysis.
        """
        self.assertFalse(credit_card_validator("22210000000000"))

    def test_53(self):
        """
        MC but with 17 digits.
        Boundary Value Analysis.
        """
        self.assertFalse(credit_card_validator("27200000000000000"))

    def test_54(self):
        """
        Visa Wrong Prefix, length, and check digit
        Error Guessing.
        """
        self.assertFalse(credit_card_validator("340000000000008"))

    def test_55(self):
        """
        MC Wrong Prefix, length, and check digit
        Error Guessing.
        """
        self.assertFalse(credit_card_validator("378282246310006"))

    def test_56(self):
        """
        AMEX Wrong Prefix, length, and check digit
        Error Guessing.
        """
        self.assertFalse(credit_card_validator("4111111111111112"))

    def test_57(self):
        """
        Visa prefix Correct, length incorrect.
        Boundary Value Anaysis
        """
        self.assertFalse(credit_card_validator("4000000000000000008"))

    def test_58(self):
        """
        Visa prefix correct, length incorrect.
        Boundary Value Analysis.
        """
        self.assertFalse(credit_card_validator("4111111111"))

    def test_59(self):
        """
        AMEX prefix correct, length incorrect.
        Boundary Value Analysis
        """
        self.assertFalse(credit_card_validator("34000000000000"))

    def test_60(self):
        """
        MC prefix correct, length incorrect.
        Boundary Value Analysis
        """
        self.assertFalse(credit_card_validator("22210000000000"))

    def test_61(self):
        """
        MC prefix correct, but length incorrect.
        Boundary Value Analysis
        """
        self.assertFalse(credit_card_validator("272000000000000000"))

    def test_62(self):
        """
        AMEX prefix correct, length correct, luhn incorrect.
        Boundary Value Analysis
        """
        self.assertFalse(credit_card_validator("340000000000008"))

    def test_63(self):
        """
        AMEX prefix correct, length correct, luhn incorrect.
        Boundary Value Analysis
        """
        self.assertFalse(credit_card_validator("340000000000091"))

    def test_64(self):
        """
        AMEX Prefix correct, length incorrect, luhn correct.
        Boundary Value Analysis
        """
        self.assertFalse(credit_card_validator("3400000000000919"))

    def test_65(self):
        """
        MC Prefix correct, length incorrect, luhn correct.
        Boundary Value Analysis
        """
        self.assertFalse(credit_card_validator("22210000000000992"))

    def test_66(self):
        """
        Visa Prefix correct, length incorrect, luhn correct.
        Boundary Value Analysis
        """
        self.assertFalse(credit_card_validator("411111111111116"))

    def test_67(self):
        """
        MC Prefix Incorrect, length Incorrect, luhn correct.
        Boundary Value Analysis
        """
        self.assertFalse(credit_card_validator("2221000000000008"))

    def test_68(self):
        """
        Visa Prefix Incorrect, length Incorrect, luhn correct.
        Boundary Value Analysis
        """
        self.assertFalse(credit_card_validator("3111111111111121"))

    def test_69(self):
        """
        AMEX Prefix Incorrect, length Incorrect, luhn correct.
        Boundary Value Analysis
        """
        self.assertFalse(credit_card_validator("3000056789512338"))

    def test_70(self):
        """
        MC Prefix Incorrect, length Correct, luhn correct.
        Partition Value Analysis
        """
        self.assertFalse(credit_card_validator("222023568912459"))


if __name__ == "__main__":
    unittest.main()
