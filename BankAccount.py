class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def printUser(self):
        print(self.name)
    

class BankAccount(User):
    def __init__ (self, name, email, acc_name='Checking'):
        User.__init__(self, name, email)
        self.int_rate = 0.01
        self.balance = 50
        self.acc_name = acc_name
        print(f'Name: {self.name}, Account Type: {self.acc_name}, Balance: ${self.balance}')
    def deposit(self, amount):
        self.balance += amount
        self.display_account_info()
        return self
    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.display_account_info()
        else:
            self.balance -= 5
            print("Sorry you have insufficient funds and will be charged $5")
            self.display_account_info()
        return self
    def display_account_info(self):
        print(f"Name: {self.name}, Account Type: {self.acc_name}, Balance: ${self.balance}")
        return self
    def yield_interest(self):
        interest = self.balance * self.int_rate
        print(f"Interest: ${interest}")
        return self

# Test to see if the Class Inheritance is set up correctly
print(issubclass(BankAccount, User))
# Set up a new User
guido = User('Guido', 'guido@email.com')
# Set up two new Accounts using the properties from User class
guidoCheck = BankAccount('Guido', 'guido@email.com')
guidoSave = BankAccount('Guido', 'guido@email.com', acc_name = 'Savings')
# Test out methods
guidoSave.deposit(50)
guidoCheck.withdrawal(25)
guidoSave.display_account_info()
guidoSave.yield_interest()
guidoSave.withdrawal(80)
# Chained
guidoSave.deposit(50).display_account_info().yield_interest().withdrawal(80)




