class account:
    def __init__(self,title=None,balance=0):
        self.title=title
        self.balance=balance

class savings_account(account):
    def __init__(self, title, balance,interest_rate):
        super().__init__(title, balance)
        self.interest_rate=interest_rate

    def __str__(self):
        return f"title is :{self.title} \naccount balance is:{self.balance} \ninterest rate is:{self.interest_rate}"

savings_account_obj=savings_account("ashish", 5000, 5)
print(savings_account_obj)
