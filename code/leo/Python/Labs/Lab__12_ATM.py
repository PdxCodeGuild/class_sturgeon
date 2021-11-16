class ATM:
    
    def __init__(self):
        self.balance = 0
        self.interest = 0.01
        self.transactions = []
    
    def check_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f'User deposited ${amount}')
        return self.balance

    def check_withdrawal(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False
        
    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f'User withdraw ${amount}')
        return self.balance

    def calc_interest(self):
        return self.balance * self.interest

    def print_transactions(self):
        return self.transactions


atm = ATM()
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
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - print transactions')
        print('exit     - exit the program')
    elif command == 'transactions':
        transactions = atm.print_transactions() # call the check_balance() method
        print(f'Your transactions {transactions}')

    elif command == 'exit':
        break
    else:
        print('Command not recognized')