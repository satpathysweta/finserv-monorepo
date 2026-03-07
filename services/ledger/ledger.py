def calculate_balance(transactions):
    if not transactions:
        return 0
    balance = 0
    for t in transactions:
        balance += t
    return balance
