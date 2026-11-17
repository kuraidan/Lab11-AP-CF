# https://github.com/kuraidan/Lab11-AP-CF
# Partner 1: Christian Fernandez
# Partner 2 : Aidan Przybylski


import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-5, 9), 4)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(-3, 2), -5)
        self.assertEqual(sub(7, -2), 9)


    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)


    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(logarithm(8, 2), 3.0)
        self.assertAlmostEqual(logarithm(10, 100), 2.0)
        self.assertAlmostEqual(logarithm(5, 1), 0.0)


    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)


    def test_multiply(self):
        self.assertEqual(mul(3,4), 12)
        self.assertEqual(mul(-3,10), -30)
        self.assertEqual(mul(0, 4), 0)

    def test_divide(self):
        self.assertEqual(div(2, 10), 5)
        self.assertAlmostEqual(div(3, 1), 1/3)
        self.assertEqual(div(9,27), 3)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2,-8)


    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-3, 4), 5)

    def test_sqrt(self):
        self.assertEqual(square_root(9), 3)
        with self.assertRaises(ValueError):
            square_root(-1)



# Do not touch this
if __name__ == "__main__":
    unittest.main()
