import src.bank_account as bank_account

account = bank_account.BankAccount('John', 500 , "business")
account_2 = bank_account.BankAccount("Dave", 1000, "personal")

account.pay_in(100)
account.pay_fee()

print(account.balance) 