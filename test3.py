file_path = "accounts.txt"


def find_line_number(file_path, account_num):
    find_line_number.line_number = 1
    with open(file_path) as filedata:
        for line in filedata:
            if account_num in line:
                return find_line_number.line_number
            find_line_number.line_number += 1
    filedata.close()
    if find_line_number.line_number == -1:
        print("Account number not found in Bank BCE records!")
    #else:
    #    print("Account information for account number {", account_num, "} is on line: ", find_line_number.line_number)


def replace_list_item(file_path, replace_string, operation):
    with open(file_path, "r") as filedata:
        lines = filedata.readlines()
    filedata.close()
    line = lines[find_line_number.line_number - 1]
    line_list = line.split(",")
    current_balance = int(line_list[6])
    if operation == "+":
        new_balance = current_balance + int(replace_string)
    elif operation == "-":
        new_balance = current_balance - int(replace_string)
    line_list[6] = str(new_balance)
    new_line = ",".join(line_list) + "\n"
    lines[find_line_number.line_number - 1] = new_line

    with open(file_path, "w") as f:
        f.writelines(lines)
    filedata.close()
    print("New account balance: ", new_balance)




def operation():
    account_num = input("What is your account number?")
    # display account information
    operation = input("Do you want to deposit, withdraw or transfer?\n type + for deposit\n type - for withdraw\n")
    if operation == "+":
        amount = str(input("How much do you want to deposit into your account?"))
        print("Depositing", amount, "...")
    elif operation == "-":
        amount = str(input("How much do you want to withdraw from your account?"))
        print("Withdrawing", amount, "...")
    else:
        print("Operator not recognized")
    find_line_number(file_path, account_num)
    replace_list_item(file_path, amount, operation)


operation()

