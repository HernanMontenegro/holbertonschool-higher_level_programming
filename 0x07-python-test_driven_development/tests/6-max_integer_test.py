import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_int(self):
        # Simple test
        self.assertAlmostEqual(max_integer([1, 19, 98]), 98)
        self.assertAlmostEqual(max_integer([13]), 13)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([7.0, 10.5, 6]), 10.5)
        self.assertAlmostEqual(max_integer([0.0]), 0.0)
