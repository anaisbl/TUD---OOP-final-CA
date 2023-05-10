import random


class Customer(object):
    def __init__(self, account_number="", account_name="", account_type="", age="", email="", address=""
                 , account_balance="0"):
        self.account_number = account_number
        self.name = account_name
        self.account_type = account_type
        self.age = age
        self.email = email
        self.address = address
        self.account_balance = account_balance

    def __str__(self):
        return "Account number: " + str(self.account_number) + "\nAccount type: " + str(self.account_type) + \
            "\nAccount name: " + str(self.name) + "\nAge: " + str(self.age) + "\nEmail: " + \
            str(self.email) + "\nAddress: " + str(self.address) + "\nAccount balance: " + str(self.account_balance)

    def write_account_to_file(self, account_info):
        f = open("accounts.txt", "a")
        f.write(",".join(account_info) + "\n")
        f.close()

    def create_account(self):
        account_type = int(input("Which account do you want to open?\n"
                                 "Type '1' for Checking; Type '2' to Savings : "))
        if account_type == 1:
            account_type = "Checking Account"
            age = int(input("How old are you? "))
            if age >= 14:
                print("Eligible to open Checking account")
                self.input_account_details(age, account_type)
            else:
                print("Too young to open Checking account")
                print("Exiting Account Creation...")
        elif account_type == 2:
            account_type = "Savings Account"
            age = int(input("How old are you? "))
            if age >= 18:
                print("Eligible to open Checking account")
                self.input_account_details(age, account_type)
            else:
                print("Too young to open Checking account")
                print("Exiting Account Creation...")

    def input_account_details(self, age, account_type):
        name = str(input("What is your name? "))
        email = str(input("How can we email you? "))
        address = str(input("Where do you live? (Street, City, Country) "))
        account_number = str(random.randint(100, 999))
        account_list = [account_number, account_type, name, str(age), email, address, self.account_balance]
        print("\nOverview Account:\n")
        self.account_number = account_list[0]
        self.account_type = account_list[1]
        self.name = account_list[2]
        self.age = account_list[3]
        self.email = account_list[4]
        self.address = account_list[5]
        self.account_balance = account_list[6]
        print(self.__str__())
        answer = str(input("Type y to confirm account, type n to cancel: "))
        if answer == "y":
            self.write_account_to_file(account_list)
            print("\nAccount created successfully\n Exiting Account Creation...\n")
        elif answer == "n":
            print("Account creation cancelled\nExiting Account Creation...\n")

    def find_account(self):
        account_number = str(input("What is your account number: "))
        account_file = "accounts.txt"

        with open(account_file, "r") as filedata:
            retrieved_line = ""
            i = 0
            for line in filedata:
                if account_number in line:
                    retrieved_line = line
                    i = i + 1
            if i == 0:
                print("Account \"" + account_number + "\" does not exist in Company BCE records !")
            else:
                print("\n---Information for account \"" + account_number + "\"---\n" + "\n")
                account_info = retrieved_line[1:-2]
                account_list = list(account_info.split(","))
                self.account_type = account_list[1]
                self.name = account_list[2]
                self.age = account_list[3]
                self.email = account_list[4]
                self.address = account_list[5]
                self.account_balance = account_list[6]
                print(self.__str__())
                self.delete_account(account_number)

    def delete_account(self, account_number):
        print("Do you want to delete your account? Type y for yes, n for no: ")
        answer = str(input("Your response:"))

        if answer == "y":
            file = open("accounts.txt", "r")
            lines = file.readlines()
            new_lines = []
            for line in lines:
                if account_number not in line.strip():
                    new_lines.append(line)
            file.close()
            file = open("accounts.txt", "w")
            file.writelines(new_lines)
            file.close()
            print("Account deleted successfully")
        elif answer == "n":
            print("no account deletion")
        else:
            print("input not recognized")
            answer = str(input("Your response:"))

    def deposit(self, amount=0):
        pass

    def withdraw(self, amount=0):
        pass


class Account(object):
    def __init__(self):
        pass


def banking_menu():
    p1 = Customer()
    p2 = Account()
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
              "1. Create Account \n"
              "2. Delete Account \n"
              "3. Withdraw money \n"
              "4. Deposit money \n"
              "5. Make a transfer\n"
              "*********************")
        answer = str(input("Your response: "))

        if answer == "1":
            p1.create_account()
        elif answer == "2":
            p1.find_account()
        elif answer == "3":
            print("withdraw money")
            break
        elif answer == "4":
            print("deposit money")
            break
        elif answer == "5":
            print("Make a transfer")
            break
        elif answer == "x":
            print("Thank you for choosing Bank CDE, bye babe!")
        else:
            print("Invalid menu option\n")

banking_menu()