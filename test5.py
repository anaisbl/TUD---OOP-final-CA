from datetime import datetime

dt = datetime.now()
ts = datetime.timestamp(dt)

#print("Date and time is: ", dt)
#print("Timestamp is: ", int(ts))

#ts_dt = datetime.fromtimestamp(ts)
#print("Timestamp to date & time: ", ts_dt)



def record_transaction(account_num, transaction_type, amount):
    ts_int = int(ts)
    transaction_list = [str(ts_int), account_num, transaction_type, amount]

    f = open("accountsTransactions.txt", "a")
    f.write(",".join(transaction_list) + "\n")
    f.close()