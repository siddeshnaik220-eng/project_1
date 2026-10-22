"""Boundary and invalid-input tests for input.py."""

import unittest

from input import validate_mark


class ValidateMarkTests(unittest.TestCase):
    def test_valid_grade_boundaries(self):
        cases = (
            ("100", "Grade boundary reached"),
            ("75", "Grade boundary reached"),
            ("74.99", "Pass"),
            ("40", "Pass"),
            ("39.99", "Fail"),
            ("0", "Fail"),
        )
        for mark, expected in cases:
            with self.subTest(mark=mark):
                self.assertEqual(validate_mark(mark), expected)

    def test_out_of_range_marks(self):
        for mark in ("-5", "105"):
            with self.subTest(mark=mark):
                self.assertEqual(validate_mark(mark), "Invalid input")

    def test_non_numeric_input(self):
        self.assertEqual(validate_mark("abc"), "Invalid numeric input")


if __name__ == "__main__":
    unittest.main()
