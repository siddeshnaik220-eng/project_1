"""Boundary-value tests for the student marks program."""

import unittest

from prog1 import grade_for, is_valid_mark


class MarksProgramTests(unittest.TestCase):
    def test_grade_cutoffs_and_values_just_below_them(self):
        # Each cutoff belongs to the higher grade; a value just below does not.
        cases = [
            (39.99, "F"),
            (40, "E"),
            (59.99, "E"),
            (60, "D"),
            (69.99, "D"),
            (70, "C"),
            (79.99, "C"),
            (80, "B"),
            (89.99, "B"),
            (90, "A"),
            (100, "A"),
        ]
        for percentage, expected_grade in cases:
            with self.subTest(percentage=percentage):
                self.assertEqual(grade_for(percentage), expected_grade)

    def test_mark_input_boundaries(self):
        self.assertTrue(is_valid_mark(0))
        self.assertTrue(is_valid_mark(100))
        self.assertFalse(is_valid_mark(-0.01))
        self.assertFalse(is_valid_mark(100.01))


if __name__ == "__main__":
    unittest.main()
