#make a bank. create two types of account - current and savings and both will inherit from Account parent class
#each account can deposit and withdraw money and can also print you a statement
#each account have different minimum limits. current account will have an overdraft of 1000 and savings account wont have an overdraft at all.

class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, not enough funds!")

    def statement(self):
        print("Account Balance: ₹{}".format(self.balance))


class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=-1000)

    def __str__(self):
        return "{}'s Current Account : Balance ₹{}".format(self.name, self.balance)


class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=0)

    def __str__(self):
        return "{}'s Savings Account : Balance ₹{}".format(self.name, self.balance)

userc = input("Enter current account holder name: ")
current_bal = int(input("Enter balance amount: "))
current_account = Current(userc, current_bal)
print(current_account)
curr_dep = int(input("Enter deposit amount: "))
current_account.deposit(curr_dep)
curr_with = int(input("Enter withdraw amount: "))
current_account.withdraw(curr_with)
current_account.statement()

usersav = input("Enter savings account holder name: ")
sav_bal = int(input("Enter amount: "))
savings_account = Savings(usersav, sav_bal)
print(savings_account)
sav_dep = int(input("Enter deposit amount: "))
savings_account.deposit(sav_dep)
sav_with = int(input("Enter withdraw amount: "))
savings_account.withdraw(sav_with)
savings_account.statement()