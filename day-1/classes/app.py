import src.bank_account as bank_account

account = {
    "holder_name": "John",
    "balance": 500,
    "type" : "business"
}

print(bank_account.get_account_name(account))