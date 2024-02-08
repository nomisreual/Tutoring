from bankaccount import BankAccount


class Bank:
    account_number_start = 1000

    def __init__(self, name: str = "", banks_accounts: dict = {}):
        self._name = name
        self._bank_accounts = banks_accounts

    def generate_account_number(self):
        self.account_number_start += 1
        return self.account_number_start


    def register(self):
        bank_account = BankAccount(account_number=self.
                                   generate_account_number())

        self._bank_accounts[bank_account._account_number] \
            = bank_account
        return f"A new account with the following account number has been created: {bank_account._account_number}"

    def retrieve(self, account_number):
        return self._bank_accounts.get(account_number)
