class ATM:     
    transactions = []

    def __init__(self):      
        self.balance = int() 
        self.i_rate = 0.01 

    def check_balance(self):
        return self.balance

    def deposit(self, amount): 
        self.balance += amount

    def check_withdrawal(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False 

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def calc_interest(self):
        return self.i_rate

    def print_transactions(self, transactions):
        print(transactions)

atm = ATM() # create an instance of our class

print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method1
        atm.transactions.append(f'user deposited ${amount}')
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            atm.transactions.append(f'user withdrew ${amount}')
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'help':
        print('Available commands:')
        print('balance      - get the current balance')
        print('deposit      - deposit money')
        print('withdraw     - withdraw money')
        print('interest     - accumulate interest')
        print('transactions - lists all transactions')
        print('exit         - exit the program')
    elif command == 'transactions':
        atm.print_transactions(atm.transactions)
    elif command == 'exit':
        break
    else:
        print('Command not recognized')