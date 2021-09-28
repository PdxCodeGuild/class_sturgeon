class ATM:
    def __init__(self, balance = 0, interest = 0.1):
        self.balance = balance
        self.interest = interest

    def check_balance(self):
        balance = self.balance
        return balance

    def deposit(self, amount):
        self.balance += amount
        return self.check_balance()

    def check_withdrawal(self, amount):
        if amount < self.check_balance():
            return True
        else:
            return False

    def withdraw(self, amount):
        if True:
            self.balance -= amount
            return self.check_balance()

    def calc_interest(self):
        i = self.balance * self.interest
        return i

    def print_transactions(history):
        history = transaction_history
        print(history)
        




transaction_history = []
atm = ATM() # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
        transaction_history.append(f'User deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'history':
        history = atm.print_transactions()
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
