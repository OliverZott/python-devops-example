import unittest

from src.velosaurus_calc.calculator import add_floats


class TestCalculator(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(add_floats(2, 3), 5)
        self.assertEqual(add_floats(-1, 1), 0)
        self.assertEqual(add_floats(0, 0), 0)
        self.assertEqual(add_floats(10, -5), 5)


if __name__ == "__main__":
    unittest.main()
