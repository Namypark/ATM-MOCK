
class Account:
    def __init__(self,category:int,balance:int=0) -> None:
        self.category = category
        self.balance= balance


    def get_deposit(self,amount:int) -> int:
        """
        amount --. type int 

        """
        if (int(amount)) < 0 :#this makes sure that the amount being deposited isnt a negative number
            raise ValueError("amount must be zero or positive")
        if not isinstance(amount,int):#makes sure it is an integer if it isnt it raises a Type Error
            raise TypeError("amount must be an integer")
        self.balance+=amount
        return self.get_balance()

    def get_withdrawal(self,amount):
        if amount > self.balance or amount < 0:#this makes sure the amount being withdrawn is not less than the actual amount and the amount being withdrawn is greater than 0
            raise ValueError("insufficient balance or type entered")
        if not isinstance(amount,int):#this ensures that a type error is raised when the amount passed isn't an integet
            raise TypeError("amount must be an integer")
        self.balance-=amount
        self.get_balance()

    
    def send_transfer(self,other,amount):#
        self.get_withdrawal(amount)#this makes sure that the money is actual removde first from the account from and before transfer it (as long as there isn't insufficient balance)
        other.get_deposit(amount)

    def get_balance(self):
        return self.balance
        

