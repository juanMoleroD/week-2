class BankAccount:
    def __init__(self, holder_name, balance, type):
        self.holder_name = holder_name
        self.balance = balance
        self.type = type
        self._rates = {
            "personal": 10,
            "business": 50
        }

    def set_name(self, new_name):
        self.holder_name = new_name

    def set_type(self, new_type):
        self.type = new_type

    def get_account_name(self):
        print(self.holder_name)
        return self.holder_name

    def pay_in(self, amount):
        self.balance += amount

    def pay_fee(self):
        if self.type == "business":
            self.balance -= 50
        elif self.type == "personal":
            self.balance -= 10
        else:
            self.balance -= 10