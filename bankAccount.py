class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount < 1:
            print("Error: Deposit amount must be at least 1 €.")
        else:
            self.balance += amount
            print(f"Successfully deposited {amount} €.")
            self.display_balance()

    def withdraw(self, amount):
        if amount < 1:
            print("Error: Withdrawal amount must be at least 1 €.")
        elif amount > self.balance:
            print("Error: Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} €.")
            self.display_balance()

    def display_balance(self):
        print(f"Current balance for {self.account_holder}: {self.balance} €.")
