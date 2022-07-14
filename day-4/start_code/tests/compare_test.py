import unittest

from src.compare import compare

class TestCompare(unittest.TestCase):

    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("3 is greater than 1", compare(3, 1))
    
    def test_compare_2_5_returns_2_is_less_than_5(self):
        self.assertEqual("2 is less than 5", compare(2,5))
    
    def test_both_numbers_are_equal(self):
        self.assertEqual("Both numbers are equal", compare(4,4))