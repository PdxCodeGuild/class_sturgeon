class Atm:

    def __init__(self):
        self.balance = int()
        self.deposit_history = []
        self.withdraw_history = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.deposit_history.append(amount)
        return self.balance

    def check_withdrawal(self, amount):
        if self.balance >= amount:
            return amount

    def withdraw(self, amount):
        self.balance = self.balance - amount
        self.withdraw_history.append(amount)
        return self.balance

    def calc_interest(self):
        amount = self.balance * 0.001
        return amount

    def print_transactions(self):
        print(f' You withdrew: ', self.withdraw_history,
              f'You deposited: ', self.deposit_history)


atm = Atm()
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance()  # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount)  # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        # call the check_withdrawal(amount) method
        if atm.check_withdrawal(amount):
            atm.withdraw(amount)  # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest()  # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')

    elif command == 'transactions':
        atm.print_transactions()

    elif command == 'exit':
        break

    else:
        print('Command not recognized')
