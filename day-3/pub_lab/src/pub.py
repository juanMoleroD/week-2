class Pub:
    def __init__(self, name, till, drinks, food):
        self.name = name
        self.till = till
        self.drinks = drinks
        self.food = food

    def increase_till(self, amount):
        self.till += amount

    def serve_drinks(self, drink, customer):
        if customer.age >= 18 and customer.drunkeness < 20:
            customer.decrease_wallet(drink.get_price())
            self.increase_till(drink.get_price())
            customer.increase_drunkeness(drink.get_alcohol_units())

    def serve_food(self, food, customer):
        customer.decrease_wallet(food.get_price())
        self.increase_till(food.get_price())
        customer.reduce_drunkeness(food.get_rejuventation_level())

    def stock_value(self):
        total_value = 0
        for drink in self.drinks:
            total_value += drink.price
        return total_value


