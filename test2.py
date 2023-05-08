def find_account():
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
            print("\n---Information for account \"" + account_number + "\"---\n" + "\n" + str(retrieved_line))
            delete_account(account_number)


def delete_account(account_number):
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



find_account()

