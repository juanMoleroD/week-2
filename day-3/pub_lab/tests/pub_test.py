import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00, [
                Drink ("Vodka", 5.00, 4), 
                Drink ("Whisky", 7.00, 5)
        ],
                Food ("Chips", 3.00, 2)
        )
        self.customer = Customer("Ally", 1000.00, 30, 0)
        

    def test_pub_has_name(self):
        actual = self.pub.name
        self.assertEqual("The Prancing Pony", actual)

    def test_pub_till_starts_100(self):
        self.assertEqual(100, self.pub.till)

    def test_can_increase_till(self):
        self.pub.increase_till(25) # ACT
        self.assertEqual(125, self.pub.till) # ASSERT

    def test_pub_has_drinks(self):
        self.assertEqual(2, len(self.pub.drinks))

    def test_ally_in_the_pub(self):
        self.assertEqual("Ally", self.customer.name)

    def test_ally_just_got_paid(self):
        self.assertEqual(1000, self.customer.wallet)

    def test_ally_just_bought_a_drink(self):
        self.pub.serve_drinks(self.pub.drinks[0], self.customer)
        self.assertEqual(105, self.pub.till)
        self.assertEqual(995, self.customer.wallet)

    def test_young_ally_cannot_buy(self):
        self.customer.age = 16
        self.pub.serve_drinks(self.pub.drinks[0], self.customer)
        self.assertEqual(100, self.pub.till)
        self.assertEqual(1000, self.customer.wallet)

    def test_ally_is_getting_tipsy(self):
        self.pub.serve_drinks(self.pub.drinks[1], self.customer)
        self.assertEqual(5, self.customer.drunkeness)

    def test_drunk_ally_refused_service(self):
        self.customer.drunkeness = 21
        self.pub.serve_drinks(self.pub.drinks[0], self.customer)
        self.assertEqual(100, self.pub.till)
        self.assertEqual(1000, self.customer.wallet)

    def test_ally_just_bought_some_food(self):
        self.pub.serve_food(self.pub.food, self.customer)
        self.assertEqual(103, self.pub.till)
        self.assertEqual(997, self.customer.wallet)

    def test_ally_is_sobering_up(self):
        self.pub.serve_drinks(self.pub.drinks[0], self.customer)
        self.pub.serve_food(self.pub.food, self.customer)
        self.assertEqual(2, self.customer.drunkeness)
        
    def test_pub_stock_value(self):
        self.assertEqual(12, self.pub.stock_value())




    

    
        

