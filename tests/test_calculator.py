import unittest

from calculator import evaluate


class CalculatorTests(unittest.TestCase):
    def test_multiplication_takes_precedence(self) -> None:
        self.assertEqual(evaluate("2 + 2 * 3"), 8)

    def test_parentheses_override_precedence(self) -> None:
        self.assertEqual(evaluate("(2 + 2) * 3"), 12)

    def test_signed_decimal_numbers_and_division(self) -> None:
        self.assertEqual(evaluate(" -1.5 + 8 / 2 - +0.5 "), 2.0)

    def test_division_by_zero(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            evaluate("5 / (2 - 2)")

    def test_rejects_invalid_or_unsupported_syntax(self) -> None:
        for expression in ("", "2 +", "e(1)", "2 ** 3", "4 // 2", "2 # comment"):
            with self.subTest(expression=expression), self.assertRaises(ValueError):
                evaluate(expression)
