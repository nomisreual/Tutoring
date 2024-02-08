class BankAccount:

    def __init__(self, account_number: int, balance=0):
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            raise Exception

    def get_balance(self):
        return self._balance
