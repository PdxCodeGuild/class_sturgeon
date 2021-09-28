# Lab 12: ATM
import time

class ATM:
    def __init__(self):
        self.balance = 0
        self.interest = .001
        self.transactions = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f'User deposited ${amount}')
        return self.balance

    def check_withdrawal(self, amount):
        if amount <= self.balance:
            return True
        else:
            self.transactions.append("User attempted to overdraw account")
            return False
    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f'User withdrew ${amount}')
        return self.balance

    def calc_interest(self):
        extra = round((self.balance * self.interest), 2)
        self.transactions.append(f'User checked account interest of ${extra}')
        return extra

    def print_transactions(self):
        print("")
        print("User Log at ATM:")
        log_rows = '\n'.join(self.transactions)
        print(log_rows)


atm = ATM() # create an instance of our class
welcome_message = 'Welcome to the ATM'
for char in welcome_message:
  print(char, end='', flush=True)
  time.sleep(.04)
time.sleep(.5)
print("")
time.sleep(.5)
while True:
    command = input('Enter a command, exit, or help: ').lower()
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
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
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
        print('log      - view log of activity')
    elif command == 'log':
        print('=============================')
        atm.print_transactions()
        print('=============================')
    elif command == 'exit':
        print('=============================')
        print("Thank you for visiting ATM")
        print('=============================')
        break
    else:
        print('Command not recognized')
