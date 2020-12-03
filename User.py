class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        if amount > 0:
            self.account_balance += amount	# the specific user's account increases by the amount of the value received
        else:
            print("ERROR: Please retry using a positive number")
        return self
    def make_withdrawal(self, amount):
        if amount > 0:
            self.account_balance -= amount
        else:
            print("ERROR: Please retry using a positive number")
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self
        



guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
guido.account_balance	# output: 300
monty.account_balance	# output: 50
guido.make_withdrawal(20)
guido.display_user_balance()	# output: Guido, 280
guido.transfer_money(monty, 25)
guido.display_user_balance()
monty.display_user_balance()
monty.make_deposit(10)
monty.display_user_balance()

# Rewritten using Chaining Methods approach with 'return self' aded to every method in the Class

guido.make_deposit(100).make_deposit(100).make_withdrawal(20).display_user_balance().transfer_money(monty, 400).display_user_balance()