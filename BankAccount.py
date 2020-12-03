class BankAccount:
    def __init__ (self, int_rate, balance=0):
        self.int_rate = 0.01
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5
            print("Sorry you have insufficient funds and will be charged $5")
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        interest = self.balance * self.int_rate
        print(f"Interest: ${interest}")
        return self

    
firstAccount = BankAccount(0.05, 200)
secondAccount = BankAccount(0.03, 150)

firstAccount.deposit(200).deposit(200).deposit(200).withdrawal(900).yield_interest().display_account_info()
secondAccount.deposit(200).deposit(200).withdrawal(50).withdrawal(30).withdrawal(50).withdrawal(30).yield_interest().display_account_info()