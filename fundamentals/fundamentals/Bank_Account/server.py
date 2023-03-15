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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # self.account = BankAccount(int_rate=0.02, balance=0)
        self.accounts = {}
        self.acc_name = ""

    def new_acct(self, int_rate, balance,  type,):
        new_account = BankAccount(int_rate, balance)
        self.accounts[type] = new_account
        self.acc_name = type

    def make_deposit(self, amount, type):
        self.accounts[type].deposit(amount)
        # self.accounts[type].balance = self.accounts[type].balance + amount
        #print(f"Account: {self.acct_num}")
        print(f"{self.acc_name} Balance: ${self.accounts[type].balance}")
        return self
    
    def make_withdraw(self, amount, type):
        self.accounts[type].withdraw(amount)
        #self.accounts[type].balance = self.accounts[type].balance - amount
        #print(f"Account: {self.acct_num}")
        print(f"{self.acc_name} Balance: ${self.accounts[type].balance}")
        return self
    
    def display_account_info(self):
        for acct_type, acct_obj in self.accounts.items():
            print(f"{acct_type} Balance: ${acct_obj.balance}")
        return self

    def yield_interest(self):
        for acct_type, acct_obj in self.accounts.items():
            if acct_obj.balance > 0:
                acct_obj.balance += (acct_obj.balance * acct_obj.int_rate)
                print(f"Your {acct_type} account balance with accumulated interest is: ${acct_obj.balance}")
            else:
                print(f"Your {acct_type} account balance is $0.")
        return self
        
    def pers_acct_info(self):
        for acct_type in self.accounts:
            print(f"Interest Rate for {acct_type}: {self.accounts[acct_type].int_rate}")
            print(f"Account Balance for {acct_type}: {self.accounts[acct_type].balance}")
        return self

    def transfer(self, person, account, deposit, withdraw):
        if account not in self.accounts:
            print("Account not found.")
            return self
        if self.accounts[account].balance < withdraw:
            print("Insufficient funds.")
            return self
        self.accounts[account].withdraw(withdraw)
        if account in person.accounts:
            person.accounts[account].deposit(deposit)
        else:
            print("Receiving account does not exist.")
            return self
        print(f"Transfered ${withdraw} from your {account} to {person.name}'s account.")
        return self

Ryan_H = User("Ryan Harvey", "ryan@ryanharvey.codes")
Christian_T = User("Christian Turner", "ct@gmail.com")
Ryan_H.new_acct(.05, 250, "Savings")
Ryan_H.make_deposit(251, "Savings")
Ryan_H.make_withdraw(13, "Savings")
Ryan_H.new_acct(.05, 250, "Checking")
Christian_T.new_acct(.05, 250, "Checking")
Ryan_H.make_deposit(53, "Checking").make_withdraw(10, "Checking")
Ryan_H.transfer(Christian_T, "Checking", 100, 100)
Ryan_H.display_account_info()



# acct_1 = BankAccount(.5, 100.01, 9998)
# acct_1.deposit(25.03).deposit(25.03).deposit(25.03).yield_interest().display_account_info()
# acct_2 = BankAccount(.25, 200.01, 9997)
# acct_2.deposit(25.03).deposit(25.03).withdraw(25.03).withdraw(25.03).withdraw(25.03).withdraw(25.03).yield_interest().display_account_info()
# acct_1.acct_info()
# acct_2.acct_info()
