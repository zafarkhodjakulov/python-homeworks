import json
import os

class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance,
        }

    @staticmethod
    def from_dict(data):
        return Account(data["account_number"], data["name"], data["balance"])

class Bank:
    def __init__(self, filename="accounts.txt"):
        self.accounts = {}
        self.filename = filename
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative.")
        account_number = len(self.accounts) + 1
        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        self.save_to_file()
        return account_number

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if not account:
            raise ValueError("Account not found.")
        return account

    def deposit(self, account_number, amount):
        account = self.view_account(account_number)
        account.deposit(amount)
        self.save_to_file()

    def withdraw(self, account_number, amount):
        account = self.view_account(account_number)
        account.withdraw(amount)
        self.save_to_file()

    def save_to_file(self):
        with open(self.filename, "w") as file:
            data = {acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}
            json.dump(data, file)

    def load_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.accounts = {int(acc_num): Account.from_dict(acc) for acc_num, acc in data.items()}

def main():
    bank = Bank()

    while True:
        print("\n--- Bank Application ---")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                name = input("Enter your name: ")
                initial_deposit = float(input("Enter initial deposit: "))
                account_number = bank.create_account(name, initial_deposit)
                print(f"Account created successfully! Your account number is {account_number}.")

            elif choice == "2":
                account_number = int(input("Enter account number: "))
                account = bank.view_account(account_number)
                print(f"Account Number: {account.account_number}")
                print(f"Name: {account.name}")
                print(f"Balance: {account.balance}")

            elif choice == "3":
                account_number = int(input("Enter account number: "))
                amount = float(input("Enter amount to deposit: "))
                bank.deposit(account_number, amount)
                print("Deposit successful.")

            elif choice == "4":
                account_number = int(input("Enter account number: "))
                amount = float(input("Enter amount to withdraw: "))
                bank.withdraw(account_number, amount)
                print("Withdrawal successful.")

            elif choice == "5":
                print("Exiting the application. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print(f"Error: {e}")

