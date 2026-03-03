def calculate_balance(transactions):
    balance = 0
    for t in transactions:
        balance += t
    return balance