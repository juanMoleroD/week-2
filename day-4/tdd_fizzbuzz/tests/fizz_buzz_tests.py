import unittest
from src.fizz_buzz import fizz_buzz

class FizzBuzzTest(unittest.TestCase):

    def test_fizz(self):
        self.assertEqual("Fizz", fizz_buzz(3))

    def test_buzz(self):
        self.assertEqual("Buzz", fizz_buzz(5))
    
    def test_fizz_buzz(self):
        self.assertEqual("FizzBuzz", fizz_buzz(15))
    
    def test_returns_number(self):
        self.assertEqual("13", fizz_buzz(13))