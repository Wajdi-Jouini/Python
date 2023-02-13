from Bank_Account import BankAccount
class Users_BankAccount(BankAccount):
    def __init__(self, name, email):
        super().__init__(int_rate=0.02, balance=0)
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(self.account.balance)
        return self
    
    def make_Withdraw(self, amount):
        self.account.withdraw(amount)
        print(self.account.balance)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        
        return self   
    # your code here
user1=Users_BankAccount("ahmed", "joui@gmail")
user1.make_deposit(500)
user1.make_Withdraw(100)
user1.display_user_balance()






