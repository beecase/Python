class Account:

    def __init__(self, amount):
        self.balance = 0
        self.deposit(amount)

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} has been deposited.")

    def withdrew(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"{amount} has been withdrawn.")

    def get_balance(self):
        print(f"Remaining balance = {self.balance}")
deposit_a = float(input("Enter the amount to be deposited: "))
account1 = Account(deposit_a)

money = float(input("Enter the money to withdraw: "))
account1.withdrew(money)

account1.get_balance()