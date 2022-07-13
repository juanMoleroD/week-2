import unittest
from src.river import River
from src.fish import Fish
from src.bear import Bear

class TestRiver(unittest.TestCase):

    def setUp(self):

        self.river = River("Nile")

        fish1 = Fish("Charlie")
        fish2 = Fish("Jorge")
        fish3 = Fish("June")

        self.fishes = [fish1, fish2, fish3]

        self.bear = Bear("Yogi", "Grizzly")
    
    def test_river_has_name(self):
        self.assertEqual("Nile", self.river.name)

    def test_river_holds_many_fish(self):
        self.river.add_fish(self.fishes[0])
        self.river.add_fish(self.fishes[1])
        self.river.add_fish(self.fishes[2])
        self.assertEqual(3, self.river.fish_count())
    
    def test_bear_can_eat_fish_from_river(self):
        self.river.add_fish(self.fishes[0])
        self.river.add_fish(self.fishes[1])
        self.bear.eat_fish_from_river(self.river)
        self.assertEqual(1, self.bear.count_food())
        self.assertEqual(1, self.river.fish_count())