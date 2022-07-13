class Drink:
    def __init__(self, name, price, alcohol_level):
       self.name = name
       self.price = price
       self.alcohol_level = alcohol_level

    def get_price(self):
        return self.price

    def get_alcohol_units(self):
        return self.alcohol_level

 