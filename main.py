from datetime import datetime
from utils import *
from account import Account

def init():
    print(datetime.today())
    q_1 = input("Do you have an account?: ")
    if q_1.lower() == 'yes':
        if login():
            operation = int(input("1.)Deposit 2.) withdraw"))
            if operation == 1:
                amount = int(input("enter amount:"))
                get_deposit(amount)
            elif operation == 2:
                amount = int(input("enter amount:"))
                get_withdrawal(amount)
        else:
            print("retry")
    else:
        write_file(*register())

print(init())