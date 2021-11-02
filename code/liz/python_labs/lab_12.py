# ATM

class ATM:

    def __init__ (self):
        self.b = int() # balance
        self.ir = 0.001 # interest rate
        self.t = [] # transactions
    
    def check_balance (self):
        return self.b
    
    def deposit (self, d):
        self.b += d
        self.t.append(f'user deposited ${d}')
    
    def check_withdrawal (self, wa):
        cw = self.b - wa # withdrawal amount
        return cw >= 0
    
    def withdraw (self, wa):
        self.b -= wa
        self.t.append(f'user withdrew ${wa}')

    def calc_interest (self):
        return self.b * self.ir
    
    def print_transactions (self):
        for i in self.t:
            print(i)



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
    elif command == 'transactions':
        transactions = atm.print_transactions() # call the print_transactions() method
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - list of transactions')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')