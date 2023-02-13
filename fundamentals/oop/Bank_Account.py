class BankAccount:
    # don't forget to add some default values for these parameters!
    all_account = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

        BankAccount.all_account.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
        # your code here 
    def withdraw(self, amount):
        if(self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
        # your code here
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
        # your code here
    def yeild_interest(self):
        if (self.balance > 0):
            self.balance += (self.balance * self.int_rate)
        return self
        # your code here


#Wajdi = BankAccount(.05,1000)
#Ahmed = BankAccount(.05,500)

#Wajdi.deposit(100).deposit(200).deposit(50).withdraw(1000).yeild_interest().display_account_info()
#Ahmed.deposit(100).deposit(300).deposit(500).withdraw(250).yeild_interest().display_account_info()


