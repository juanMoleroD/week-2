from unicodedata import name
import unittest
from src.fish import Fish

class TestFish(unittest.TestCase):
    
    def setUp(self):
        fish1 = Fish("Charlie")
        fish2 = Fish("Jorge")
        fish3 = Fish("June")

        self.fishes = [fish1, fish2, fish3]
        
    def test_fish_has_name(self):
        self.assertEqual("Charlie", self.fishes[0].name)