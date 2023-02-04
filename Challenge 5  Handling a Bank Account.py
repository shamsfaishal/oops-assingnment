class account:
    def __init__(self,balance=0,title=None,amount=0):
        self.title=title
        self.balance=balance
        self.amount=amount
        
    def deposit(self,amount):
        self.balance=self.balance+ amount
        
    def withdrawal(self,amount):
        self.balance=self.balance-amount
        
    def get_balance(self):
        return self.balance

class savings_account(account):
    def __init__(self,balance=0,title= None,interest_rate=0):
        super().__init__(title,balance)
        
        self.interest_rate=interest_rate

    def interest_amount(self):
        return (self.interest_rate*self.balance)/100

demo=account(2000)
demo.withdrawal(500)
print(demo.get_balance())

demo=account(2000)
demo.deposit(500)
print(demo.get_balance())

demo1=savings_account("ashish",2000,5)
print(demo1.interest_amount())
    
