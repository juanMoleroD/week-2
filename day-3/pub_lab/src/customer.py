class Customer:
    def __init__(self, name, wallet, age, drunkeness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkeness = drunkeness

    def decrease_wallet(self, price):
        self.wallet -= price

    def increase_drunkeness(self, level):
        self.drunkeness += level

    def reduce_drunkeness(self, amount):
        self.drunkeness -= amount


