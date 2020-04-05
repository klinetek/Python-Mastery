class Account:
    """ Simple account class with balance """

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("You cannot withdraw you more than what you have...")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.balance))


if __name__ == '__main__':
    #because of the print in the init this will show that print with these values
    Dustin = Account("Dustin", 0)
    Dustin.deposit(1000)
    Dustin.withdraw(5000)
