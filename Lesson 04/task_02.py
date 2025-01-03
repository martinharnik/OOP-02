class Account:
    def __init__(self, act_num, balance):
        self.act_num = act_num
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Not enough funds.")

    def get_balance(self):
        return self.balance

class InterestAccount(Account):
    def __init__(self, act_num, balance, interest_rate):
        super().__init__(act_num, balance)
        self.interest_rate = interest_rate

    def calc_interest(self):
        return self.balance * self.interest_rate
    
class Transactions:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def history(self):
        for transaction in self.transactions:
            print(transaction)

class SavingsAccount(InterestAccount, Transactions):
    def __init__(self, act_num, balance, interest_rate):
        InterestAccount.__init__(self, act_num, balance, interest_rate)
        Transactions.__init__(self)


savings = SavingsAccount("SA001", 5000, 0.08)
savings.deposit(2500)
savings.withdraw(650)

print(savings.calc_interest())

print(savings.get_balance())

savings.add_transaction("Deposit: 2500")
savings.add_transaction("Withdrawl: 650")

savings.history()