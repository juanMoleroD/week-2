class Food:
    def __init__(self, name, price, rejuventation_level):
       self.name = name
       self.price = price
       self.rejuventation_level = rejuventation_level

    def get_price(self):
        return self.price

    def get_rejuventation_level(self):
        return self.rejuventation_level