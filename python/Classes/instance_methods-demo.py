class BankAccount:
    def __init__(self,owner):
        self.owner = owner
        self.balance = 0.0

    def getBalance(self):
        return f"Your balance is {self.balance}"
    
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self,amount):
        self.balance -= amount
        if (amount > self.balance):
            print("You can't withraw.. insufficient funds ")

account = BankAccount("Kaan")

print(account.deposit(1000))
print(account.getBalance())

print(account.withdraw(1300))