"""Boundary-value tests for the student marks program (standard library only)."""

import unittest

from stru import grade_for, is_valid_mark


class StudentMarksTests(unittest.TestCase):
    def test_mark_boundaries(self):
        # The endpoints are valid; values just outside the range are not.
        self.assertTrue(is_valid_mark(0))
        self.assertTrue(is_valid_mark(100))
        self.assertFalse(is_valid_mark(-0.01))
        self.assertFalse(is_valid_mark(100.01))

    def test_grade_boundaries(self):
        # A boundary earns that grade; a value just below earns the lower grade.
        cases = (
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
        )
        for percentage, expected_grade in cases:
            with self.subTest(percentage=percentage):
                self.assertEqual(grade_for(percentage), expected_grade)


if __name__ == "__main__":
    unittest.main()
