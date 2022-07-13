import unittest
from src.bear import Bear
from src.fish import Fish

class TestBear(unittest.TestCase):
    
    def setUp(self):

        bear1 = Bear("Yogy", "Grizzly")
        bear2 = Bear("Bubbu", "Brown")

        self.bears = [bear1, bear2]

        fish1 = Fish("Charlie")
        fish2 = Fish("Jorge")
        fish3 = Fish("June")

        self.fishes = [fish1, fish2, fish3]

    def test_bear_has_name(self):
        self.assertEqual("Yogy", self.bears[0].name)
    
    def test_bear_has_type(self):
        self.assertEqual("Grizzly", self.bears[0].type)

    def test_bear_has_empty_stomach(self):
        self.assertEqual([], self.bears[1].stomach)
    
    def test_bear_can_eat_fish(self):
        self.bears[0].eat_fish(self.fishes[0])
        self.assertEqual([self.fishes[0]], self.bears[0].stomach)
    
    def test_bear_can_count_food(self):
        self.bears[0].eat_fish(self.fishes[0])
        self.assertEqual(1, self.bears[0].count_food())
