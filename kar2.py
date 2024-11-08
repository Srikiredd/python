class BankAccount:
    def __init__(self, account_id, initial_balance=0):
        self.account_id = account_id
        if initial_balance < 0:
            print("Error: Sorry! The balance cannot be negative.")
            self.balance = 0
        else:
            self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful. New Balance: ${self.balance:.2f}")
        else:
            print("Error: Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Error: Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. New Balance: ${self.balance:.2f}")
    
    def fixed_deposit(self, amount):
        if amount > 500000:
            print("In Jyothi Bank, we cannot accept cash deposits over 5 lakhs; please switch to a fixed deposit.")
        elif self.balance > 500000:
            print("Amount is too high; please switch to a fixed deposit.")
        else:
            print(f"Fixed deposit of ${amount:.2f} is successful. This feature can be expanded with more logic.")

    def check_balance(self):
        return self.balance


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id, initial_balance=0):
        if account_id in self.accounts:
            print("Error: Account with this ID already exists.")
        else:
            self.accounts[account_id] = BankAccount(account_id, initial_balance)
            print(f"Account {account_id} created successfully with balance ${initial_balance:.2f}")

    def access_account(self, account_id):
        account = self.accounts.get(account_id)
        if account:
            return account
        else:
            print("Error: Account not found.")
            return None

    def show_menu(self):
        print("\nBank Menu:")
        print("1. Create Account")
        print("2. Access Account")
        print("3. Exit")

    def account_menu(self, account):
        print("\nAccount Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")
        print("5. Fixed Deposit")

        while True:
            try:
                choice = int(input("Please select an option: "))
                if choice == 1:
                    print(f"Current Balance: ${account.check_balance():.2f}")
                elif choice == 2:
                    amount = float(input("Enter amount to deposit: $"))
                    account.deposit(amount)
                elif choice == 3:
                    amount = float(input("Enter amount to withdraw: $"))
                    account.withdraw(amount)
                elif choice == 4:
                    print("Logging out of account.")
                    break
                elif choice == 5:
                    amount = float(input("Enter amount for fixed deposit: $"))
                    account.fixed_deposit(amount)
                else:
                    print("Error: Invalid choice. Please select a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def start(self):
        while True:
            self.show_menu()
            try:
                choice = int(input("Please select an option: "))
                if choice == 1:
                    account_id = input("Enter new account ID: ")
                    initial_balance = float(input("Enter initial balance: "))
                    self.create_account(account_id, initial_balance)
                elif choice == 2:
                    account_id = input("Enter account ID to access: ")
                    account = self.access_account(account_id)
                    if account:
                        self.account_menu(account)
                elif choice == 3:
                    print("Thank you for using our Bank services.")
                    break
                else:
                    print("Error: Invalid choice. Please select a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    bank = Bank()
    bank.start()













