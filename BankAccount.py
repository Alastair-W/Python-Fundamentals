class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    # updating all transactional methods from User class to BankAccount class
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        if amount > 0:
            self.account.deposit(amount)	# the specific user's account increases by the amount of the value received
            print(f"Balance: ${self.account.balance}")
        else:
            print("ERROR: Please retry using a positive number")
        return self
    def make_withdrawal(self, amount):
        if amount > 0:
            self.account.withdrawal(amount)
            print(f"Balance: ${self.account.balance}")
        else:
            print("ERROR: Please retry using a positive number")
        return self
    def display_user_balance(self):
        self.account.display_account_info()
        return self
    def transfer_money(self, other_user, amount):
        self.account.withdrawal(amount)
        other_user.account.deposit(amount)
        return self

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

    
# firstAccount = BankAccount(0.05, 200)
# secondAccount = BankAccount(0.03, 150)

# firstAccount.deposit(200).deposit(200).deposit(200).withdrawal(900).yield_interest().display_account_info()
# secondAccount.deposit(200).deposit(200).withdrawal(50).withdrawal(30).withdrawal(50).withdrawal(30).yield_interest().display_account_info()

guido = User('Guido', 'guido@email.com')


guido.make_deposit(-100).make_withdrawal(10).display_user_balance()