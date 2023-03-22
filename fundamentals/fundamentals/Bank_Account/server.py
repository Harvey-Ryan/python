from models.bank_account import BankAccount;
from models.users import User;

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