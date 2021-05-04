
import json
import os
from random import randrange


def read_account(filename:str):
    if not os.path.exists(filename):
        print("does not exist")
    else:
        with open(filename,'r') as file:
            data = json.load(file)
            return data

def write_file(first_name,last_name,account_number,email,password):
    if not os.path.exists(f"{account_number}.json"):
        user_details = {
                'first_name':first_name,
                'last_name':last_name,
                'account_number':account_number,
                'email':email,
                'password':password,
                'balance':0
                }
                
        with open(f"{account_number}.json",'w') as file:
            data = json.dump(user_details,file,indent=4)
    else:
        print('File exists')

def generate_account_number():
    return randrange(0,9999999999)

def register():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    email = input("Enter your email: ")
    password = input("Enter Password: ")
    while len(password) != 4:
        print("please make sure your password 4 digits")
        password = input("Enter Password: ")
    
    try:
        account_number = generate_account_number()
    except ValueError:
        raise ValueError("Ensure your password is not in strings")
    
    return first_name, last_name, str(account_number), email, password

def login():
    try:
        user = input("Account number:")
        password = input("password: ")
        user_details = read_account(f"{user}.json")
        if user_details['account_number'] !=user or user_details['password'] != password:
            return('invalid credentials')
        else:
            return(f"welcome {user_details['first_name']}..\n")
    except TypeError:
        pass

def get_deposit(amount:int,balance=0) -> int:
    """
    amount --. type int 
    """
    if (int(amount)) < 0 :#this makes sure that the amount being deposited isnt a negative number
        raise ValueError("amount must be zero or positive")
    if not isinstance(amount,int):#makes sure it is an integer if it isnt it raises a Type Error
        raise TypeError("amount must be an integer")
    balance+=amount
    print(balance)

def get_withdrawal(amount,balance=0):
    if amount > balance or amount < 0:#this makes sure the amount being withdrawn is not less than the actual amount and the amount being withdrawn is greater than 0
        raise ValueError("insufficient balance or type entered")
    if not isinstance(amount,int):#this ensures that a type error is raised when the amount passed isn't an integet
        raise TypeError("amount must be an integer")
    balance-=amount
    print(balance)