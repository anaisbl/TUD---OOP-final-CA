import os
from datetime import datetime, timedelta


class Transaction:
    transactions = []

    def __init__(self, transaction_id, account_id, amount, timestamp):
        self.transaction_id = transaction_id
        self.account_id = account_id
        self.amount = amount

        dt = datetime.now()
        ts = datetime.timestamp(dt)
        ts_int = int(ts)
        self.timestamp = ts_int

        # append transaction object to list transaction
        Transaction.transactions.append(self)

    def save_transaction(self):
        with open("accountsTransactions.txt", "a") as file:
            file.write("{},{},{},{}\n".format(self.transaction_id, self.account_id, self.amount, self.timestamp))

    @staticmethod
    def new(account, amount):
        # create transaction to be saved to accountsTransactions.txt
        new_transaction = Transaction(len(Transaction.transactions), account.id, amount, datetime.now())
        # call method to save new transaction
        new_transaction.save_transaction()
        return new_transaction  # to credit_transaction and debit_transaction

    @staticmethod
    def read_transactions():
        # check file exists
        if not os.path.exists("accountsTransactions.txt"):
            return
        with open("accountsTransactions.txt", "r") as file:
            for line in file:
                transaction_data = line.strip().split(",")
                # passes information to constructor
                Transaction(transaction_data[0], transaction_data[1], transaction_data[2],
                                          transaction_data[3])

    @staticmethod
    def find_account_transactions(account_id):
        account_transactions = []
        for transaction in Transaction.transactions:
            if transaction.account_id == account_id:
                account_transactions.append(transaction)
        return account_transactions


class Account:
    accounts = []

    # Used when creating a new account
    def __init__(self, account_id, customer_id, balance, closed = False):
        self.id = int(account_id)
        self.customer_id = int(customer_id)
        self.balance = float(balance)
        self.closed = closed
        Account.accounts.append(self)

    # Used to print the type of account
    def get_type(self):
        pass

    def deposit(self, amount):
        self.balance = self.balance + amount
        Transaction.new(self, amount)  # calls the method to record the transaction in accountsTransactions.txt
        print("\nNew account balance: ", self.balance)
        Account.save_accounts()  # calls method to save updated balance to accounts.txt

    def withdraw(self, amount):
        self.balance = self.balance - amount
        Transaction.new(self, -amount) # calls the method to record the transaction in accountsTransactions.txt
        print("\nNew account balance: ", self.balance)
        Account.save_accounts()  # calls method to save updated balance to accounts.txt

    def transfer(self, recipient_account_id, amount):
        recipient_account = None  #
        for account in Account.accounts:
            if account.id == recipient_account_id:
                recipient_account = account
                break
        
        if recipient_account is None:
            print("Recipient account with ID {} does not exist.".format(recipient_account_id))
            return
        
        if self.balance >= amount:
            self.balance = self.balance - amount
            recipient_account.balance += amount
            Transaction.new(self, -amount)
            Transaction.new(recipient_account, amount)
            print("Transfer of amount {} from Account {} to Account {} completed.".format(amount, self.id, recipient_account.id))
            Account.save_accounts()
        else:
            print("Insufficient balance in Account {} for the transfer.".format(self.id))

    def print_transactions(self):
        transactions = Transaction.find_account_transactions(self.id)
        for index, transaction in enumerate(transactions):
            print("[{}]: Amount: {}".format(index, transaction.amount))

    def close(self):
        self.closed = True
        Account.save_accounts()
        print("\nAccount successfully closed\n")

    @staticmethod
    def find_customer_accounts(customer):
        customer_accounts = []
        for account in Account.accounts:
            if account.closed == True:
                continue
            if account.customer_id == customer.id:
                customer_accounts.append(account)
        return customer_accounts

    @staticmethod
    def save_accounts():
        with open("accounts.txt", "w") as file:
            for account in Account.accounts:
                file.write("{},{},{},{},{}\n".format(account.id, account.customer_id, account.balance, account.closed, account.get_type()))

    @staticmethod
    def read_accounts():
        # check file exists
        if not os.path.exists("accounts.txt"):
            return
        with open("accounts.txt", "r") as file:
            try:
                for line in file:
                    account = None
                    account_data = line.strip().split(",")
                    account_type = account_data[4]

                    if account_type == "Checking":
                        CheckingAccount(account_data[0], account_data[1], account_data[2],
                                        account_data[3] == "True")

                    elif account_type == "Savings":
                        SavingsAccount(account_data[0], account_data[1], account_data[2],
                                       account_data[3] == "True")
                    else:
                        print("Unknown account type")
            except:
                print("Error reading account from file")


class CheckingAccount(Account):
    def transfer(self, recipient_account_id, amount):
        new_balance = self.balance - amount
        if new_balance < -200:
            print("Transfer exceeds credit limit of -200€!. Try another amount.")
        else:
            super().transfer(recipient_account_id, amount)

    def withdraw(self, amount):
        new_balance = self.balance - amount
        if new_balance < -200:
            print("Credit limit of -200€ reached! Cannot withdraw. Try another amount.")
        else:
            super().withdraw(amount)

    def get_type(self):
        return "Checking"

    @staticmethod
    def new_account(customer):
        new_account = CheckingAccount(len(Account.accounts), customer.id, 0)
        Account.save_accounts()
        return new_account


class SavingsAccount(Account):
    def transfer(self, recipient_account_id, amount):
        new_balance = self.balance - amount
        if new_balance < 0:
            print("You cannot have a negative balance!")
        else:
            super().transfer(recipient_account_id, amount)

    def withdraw(self, amount):
        new_balance = self.balance - amount
        if new_balance < 0:
            print("You cannot withdraw below negative balance!")
        else:
            super().withdraw(amount)

    def can_perform_transaction(self):
        current_date = datetime.now()
        one_month_ago = current_date - timedelta(days=30)
        for transaction in Transaction.find_account_transactions(self.id):
            if transaction.amount < 0 and transaction.timestamp >= one_month_ago:
                return True
        return False

    def get_type(self):
        return "Savings"

    @staticmethod
    def new_account(customer):
        new_account = SavingsAccount(len(Account.accounts), customer.id, 0)
        Account.save_accounts()
        return new_account


class Customer(object):
    customers = []

    def __init__(self, customer_id, name, age, email, address):
        self.name = name
        self.age = int(age)
        self.email = email
        self.address = address
        self.id = int(customer_id)
        # append customer object to customer list
        Customer.customers.append(self)

    @staticmethod
    def new_customer(name, age, email, address):
        customer_id = len(Customer.customers)
        new_customer = Customer(customer_id, name, age, email, address)
        Customer.save_customers()
        return new_customer

    def create_account(self):
        account_type = int(input("Which account do you want to open?\n"
                                 "Type '1' for Checking; Type '2' to Savings : "))
        if account_type == 1:
            if self.age >= 18:
                CheckingAccount.new_account(self)
                print("You have opened a Checking account successfully!")
            else:
                print("Too young to open Checking account")
                print("Exiting Account Creation...")
        elif account_type == 2:
            if self.age >= 14:
                SavingsAccount.new_account(self)
                print("You have opened a Savings account successfully!")
            else:
                print("Too young to open Savings account")
                print("Exiting Account Creation...")

    @staticmethod
    def read_customers():
        if not os.path.exists("customers.txt"):
            return
        with open("customers.txt", "r") as file:
            for line in file:
                customer_data = line.strip().split(",")
                Customer(customer_data[0], customer_data[1], customer_data[2], customer_data[3], customer_data[4])

    @staticmethod
    def save_customers():
        with open("customers.txt", "w") as file:
            for customer in Customer.customers:
                file.write("{},{},{},{},{}\n".format(customer.id, customer.name, customer.age, customer.email, customer.address))

class BankMenu:
    customer = None

    @staticmethod
    def main_menu():
        Customer.read_customers()
        Account.read_accounts()
        Transaction.read_transactions()

        answer = ""
        while answer != "x":
            print("*********************\n"
                   "BANK CDE MENU \n"
                   "Welcome to Bank CDE services \n"
                   "How can we help you today?\n"
                   "*********************\n"
                   "Enter the number corresponding to the option you want \n"
                   "To exit, enter x\n"
                   "*********************\n"
                   "1. Sign Up \n"
                   "2. Login \n"
                   "*********************")
            answer = str(input("Your response: "))

            if answer == "1":
                BankMenu.customer_create_menu()
            elif answer == "2":
                BankMenu.customer_login_menu()
            elif answer == "x":
                print("Thank you for choosing Bank CDE, bye babe!")
            else:
                print("Invalid menu option\n")

    @staticmethod
    def customer_create_menu():
        name = str(input("What is your name? "))
        email = str(input("How can we email you? "))
        address = str(input("Where do you live? (City Country) "))
        age = int(input("How old are you?"))

        new_customer = Customer.new_customer(name, age, email, address)

        print("New customer created with id: " + str(new_customer.id))
        input("Press Enter to Continue... ")

    @staticmethod
    def customer_login_menu():
        customer_id = int(input("Please enter customer id: "))
        
        # Check if the customer exists
        customer = None
        for c in Customer.customers:
            if c.id == customer_id:
                customer = c
                break
        
        if customer is None:
            print("Customer with ID {} does not exist.".format(customer_id))
            return
        
        BankMenu.customer = customer
        BankMenu.customer_menu()

    @staticmethod
    def customer_menu():
        # Customer exists, proceed with login
        customer = BankMenu.customer
        print("Welcome, {}!".format(customer.name))
        
        while True:
            print("\n*********************\n"
                  "Customer Menu\n"
                  "*********************\n"
                  "1. Create Account\n"
                  "2. Find Account\n"
                  "x. Logout\n"
                  "*********************")
            
            answer = str(input("Your response: "))
            
            if answer == "1":
                customer.create_account()
            elif answer == "2":
                BankMenu.view_accounts_menu()
            elif answer == "x":
                print("Logged out.")
                break
            else:
                print("Invalid menu option.")

    @staticmethod
    def view_accounts_menu():
        customer = BankMenu.customer

        # Check if the customer has any accounts
        customer_accounts = Account.find_customer_accounts(customer)
        if not customer_accounts:
            print("No accounts found for customer {}.".format(customer.name))
            return

        print("\n*********************\n"
              "Accounts Menu\n"
              "*********************")

        while True:
            print("Customer: {}\n".format(customer.name))

            # Display customer's accounts
            print("Accounts:")
            for index, account in enumerate(customer_accounts):
                print("[{}] ({}): Account ID: {}, Balance: {}".format(index+1, account.get_type(), account.id, account.balance))

            print("\nPlease select an account.")
            print("Enter 'x' to go back to the Customer Menu.")

            answer = input("Your response: ")

            if answer == "x":
                break

            try:
                index = int(answer) - 1
                selected_account = customer_accounts[index]

                BankMenu.account_menu(selected_account)
                break

            except (ValueError, IndexError):
                print("Invalid selection. Please try again.")

    @staticmethod
    def account_menu(account):
        print("\n*********************\n"
              "Account Menu\n"
              "*********************")

        while True:
            print("Account ID: {}".format(account.id))
            print("Balance: {}\n".format(account.balance))

            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. View Transactions")
            print("5. Delete")
            print("x. Go back to Accounts Menu")

            answer = input("Your response: ")

            if answer == "1":
                amount = int(input("Enter the amount to deposit: "))
                account.deposit(amount)
            elif answer == "2":
                amount = int(input("Enter the amount to withdraw: "))
                account.withdraw(amount)
            elif answer == "3":
                recipient_account_id = int(input("Enter the recipient account ID: "))
                amount = int(input("Enter the amount to transfer: "))
                account.transfer(recipient_account_id, amount)
            elif answer == "4":
                account.print_transactions()
            elif answer == "5":
                account.close()
                break
            elif answer == "x":
                break
            else:
                print("Invalid menu option.")


BankMenu.main_menu()
