class Account:
    def _init_(self, account_number, pin, balance=0.0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def record_transaction(self, transaction_type, amount):
        self.transaction_history.append((transaction_type, amount))

    def get_transaction_history(self):
        return self.transaction_history

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.record_transaction('Deposit', amount)
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.record_transaction('Withdrawal', amount)
            return True
        else:
            return False

class ATM:
    def _init_(self):
        self.accounts = {}
        self.current_account = None

    def create_account(self, account_number, pin, initial_deposit=0.0):
        if account_number in self.accounts:
            print("Account already exists.")
            return False
        else:
            self.accounts[account_number] = Account(account_number, pin, initial_deposit)
            print(f"Account {account_number} created successfully.")
            return True

    def authenticate(self, account_number, pin):
        account = self.accounts.get(account_number)
        if account and account.pin == pin:
            self.current_account = account
            return True
        else:
            return False

    def show_menu(self):
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Transaction History")
        print("5. Exit")

    def main(self):
        while True:
            print("\nWelcome to the ATM")
            account_number = input("Enter your account number: ")
            pin = input("Enter your PIN: ")

            if self.authenticate(account_number, pin):
                print("Authentication successful.\n")
                while True:
                    self.show_menu()
                    choice = input("Choose an option: ")

                    if choice == '1':
                        print(f"Your balance is: ${self.current_account.check_balance():.2f}")
                    elif choice == '2':
                        try:
                            amount = float(input("Enter amount to deposit: "))
                            if self.current_account.deposit(amount):
                                print("Deposit successful.")
                            else:
                                print("Invalid amount.")
                        except ValueError:
                            print("Invalid input. Please enter a numeric value.")
                    elif choice == '3':
                        try:
                            amount = float(input("Enter amount to withdraw: "))
                            if self.current_account.withdraw(amount):
                                print("Withdrawal successful.")
                            else:
                                print("Insufficient funds or invalid amount.")
                        except ValueError:
                            print("Invalid input. Please enter a numeric value.")
                    elif choice == '4':
                        history = self.current_account.get_transaction_history()
                        print("\nTransaction History:")
                        for transaction in history:
                            print(f"{transaction[0]} of ${transaction[1]:.2f}")
                    elif choice == '5':
                        self.current_account = None
                        print("Thank you for using the ATM.")
                        break
                    else:
                        print("Invalid option. Please try again.")
            else:
                print("Authentication failed. Please try again.")

if _name_ == "_main_":
    atm = ATM()
    atm.create_account("123456", "1234", 1000.0)
    atm.create_account("654321", "4321", 500.0)
    atm.main()
