from bank import Bank


def main():

    bank = Bank(name="DCI Bank")
    menu = {
        "1": "Create a new account.",
        "2": "Deposit funds into an account.",
        "3": "Withdraw funds from an account.",
        "4": "Check the balance of an account.",
        "5": "Exit the program.",
    }

    print(f"Welcome to {bank._name}. How can we help you today?")

    while True:

        for key, value in menu.items():
            print(f"{key}: {value}")

        selection = input("Please select an option: ")

        try:
            selection = int(selection)
        except ValueError:
            print("Please select a valid choice.")
            continue

        match selection:
            case 1:
                message = bank.register()
                print(message)
            case 2:
                while True:
                    account_number = input(
                        "Please enter your account number: ")
                    try:
                        account_number = int(account_number)
                    except ValueError:
                        print("Please enter a valid number.")
                        continue

                    bank_account = bank.retrieve(account_number)
                    if bank_account:
                        break
                    else:
                        print(
                            "I am sorry, there is no account for the provided number. You will be asked to enter an account number again.")
                        continue

                while True:
                    amount = input(
                        "How much would you like to deposit (only integers)? ")
                    try:
                        amount = int(amount)
                        break
                    except ValueError:
                        print("Plase enter a valid amount (no decimals).")
                        continue
                bank_account.deposit(amount)
                print(f"{amount} have been deposited.")

            case 3:
                while True:
                    account_number = input(
                        "Please enter your account number: ")
                    try:
                        account_number = int(account_number)
                    except ValueError:
                        print("Please enter a valid number.")
                        continue

                    bank_account = bank.retrieve(account_number)
                    if bank_account:
                        break
                    else:
                        print(
                            "I am sorry, there is no account for the provided number. You will be asked to enter an account number again.")
                        continue

                while True:
                    amount = input(
                        "How much would you like to withdraw (only integers)? ")
                    try:
                        amount = int(amount)
                    except ValueError:
                        print("Plase enter a valid amount (no decimals).")
                        continue

                    try:
                        bank_account.withdraw(amount)
                        print(f"{amount} have been withdrawn.")
                        print(
                            f"Your new balance is {bank_account.get_balance()}")
                    except:
                        print("I am sorry, you cannot withdraw that much.")
                        print(
                            f"Your current balance is {bank_account.get_balance()}")
                        continue
                    break

            case 4:
                while True:
                    account_number = input(
                        "Please enter your account number: ")
                    try:
                        account_number = int(account_number)
                    except ValueError:
                        print("Please enter a valid number.")
                        continue

                    bank_account = bank.retrieve(account_number)
                    if bank_account:
                        break
                    else:
                        print(
                            "I am sorry, there is no account for the provided number. You will be asked to enter an account number again.")
                        continue
                current_balance = bank_account.get_balance()
                print(f"Your current balance is: {current_balance}")
            case 5:
                print("Thank you for your visit. The data has been stored only for the runtime of the program. Your savings are lost LOL!")
                break


if __name__ == "__main__":
    main()
