class Account(object):
    def __init__(self, account_type="", name="", age="", email="", address=""):
        self.account_type = account_type
        self.name = name
        self.age = age
        self.email = email
        self.address = address

    def __str__(self):
        return "Account type: " + str(self.account_type) + "\nAccount name: " + str(self.name) + \
            "\nAge: " + str(self.age) + "\nEmail: " + str(self.email) + "\nAddress: " + str(self.address)

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


p1 = Account()
p1.find_account()

