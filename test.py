import random


class Account(object):
    def __init__(self, account_number=0, account_name="", account_type="", age=0, email="", address=""):
        self.account_number = account_number
        self.account_name = account_name
        self.account_type = account_type
        self.age = age
        self.email = email
        self.address = address

    def create_account(self):
        pass

    def deposit(self, amount=0):
        pass

    def withdraw(self, amount=0):
        pass

    class SavingAccount(object):
        pass

    class CurrentAccount(object):
        def transfer(self, amount=0, destination=""):
            pass


class Customer(object):
    def __init__(self):
        pass


p1 = Account()
p1.create_account()
