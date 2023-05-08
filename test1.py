import random


def write_account_to_file(account_info):
    f = open("accounts.txt", "a")
    f.write(str(account_info) + "\n")
    f.close()


def create_account():
    account_type = int(input("Which account do you want to open?\n"
                             "Type '1' for Checking; Type '2' to Savings : "))
    if account_type == 1:
        account_type = "Checking Account"
        age = int(input("How old are you? "))
        if age > 14:
            print("Eligible to open Checking account")
            input_account_details(age, account_type)
        else:
            print("Too young to open Checking account")
            print("Exiting Bank CDE menu...")
    elif account_type == 2:
        account_type = "Savings Account"
        age = int(input("How old are you? "))
        if age > 18:
            print("Eligible to open Checking account")
            input_account_details(age, account_type)
        else:
            print("Too young to open Checking account")
            print("Exiting Bank CDE menu...")


def input_account_details(age, account_type):
    name = str(input("What is your name? "))
    email = str(input("How can we email you? "))
    address = str(input("Where do you live? (Street, City, Country) "))
    account_number = random.randint(100, 999)
    account_list = [account_number, account_type, name, age, email, address]
    write_account_to_file(account_list)
    print(account_list, "Account created successfully")


def banking_menu():
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
            create_account()
            break
        elif answer == "2":
            print("delete account")
            break
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
