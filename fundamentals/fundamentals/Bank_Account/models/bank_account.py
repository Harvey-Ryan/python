class BankAccount:

    # def __init__(self, int_rate, balance, acct_num):
    def __init__(self, int_rate, balance):

        #self.acct_num = acct_num
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        #print(f"Account: {self.acct_num}")
        #print(f"Balance: ${self.balance}")
        return self
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        #print(f"Account: {self.acct_num}")
        #print(f"Balance: ${self.balance}")
        return self
    
    def display_account_info(self):
        #print(f"Account: {self.acct_num}")
        #print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
            #print(f"Account: {self.acct_num}")
            #print(f"Your balance with accumulated interest is: ${self.balance}")
            return self
        else:
            #print(f"Account: {self.acct_num}")
            #print(f"$0 balance.")
            return self
        
    def acct_info(self):
        print(f"Account Number: {self.acct_num}")
        print(f"Interest Rate: {self.int_rate}")
        print(f"Account Balance: {self.balance}")
