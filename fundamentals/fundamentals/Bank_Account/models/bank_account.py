class BankAccount:

    def __init__(self, int_rate, balance):

        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self
    
    def display_account_info(self):
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
            return self
        else:
            return self
        
    def acct_info(self):
        print(f"Account Number: {self.acct_num}")
        print(f"Interest Rate: {self.int_rate}")
        print(f"Account Balance: {self.balance}")
