class ATM {
    
    constructor(balance=0) {
        this.balance = balance
        this.transactions = []
    }
          
    check_balance() {
        return this.balance
    }
    
    deposit(amount) {
        this.balance += amount
        this.transactions.push(`User deposited ${amount}`)
        return this.balance
    }

    check_withdrawal(amount) {
        if (this.balance >= amount) {
            return true 
        }
        else {
            return false
        }
    }
        
    withdraw(amount) {
        this.balance -= amount
        this.transactions.push(`User withdraw ${amount}`)
        return this.balance
    }

    calc_interest() {
        return this.balance * 0.01
    }

    print_transactions() {
        return this.transactions
    }

}

let atm = new ATM()

// while True:
//     command = input('Enter a command: ')
//     if command == 'balance':
//         balance = atm.check_balance() # call the check_balance() method
//         print(f'Your balance is ${balance}')
//     elif command == 'deposit':
//         amount = float(input('How much would you like to deposit? '))
//         atm.deposit(amount) # call the deposit(amount) method
//         print(f'Deposited ${amount}')
//     elif command == 'withdraw':
//         amount = float(input('How much would you like '))
//         if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
//             atm.withdraw(amount) # call the withdraw(amount) method
//             print(f'Withdrew ${amount}')
//         else:
//             print('Insufficient funds')
//     elif command == 'interest':
//         amount = atm.calc_interest() # call the calc_interest() method
//         atm.deposit(amount)
//         print(f'Accumulated ${amount} in interest')
//     elif command == 'help':
//         print('Available commands:')
//         print('balance  - get the current balance')
//         print('deposit  - deposit money')
//         print('withdraw - withdraw money')
//         print('interest - accumulate interest')
//         print('transactions - print transactions')
//         print('exit     - exit the program')
//     elif command == 'transactions':
//         transactions = atm.print_transactions() # call the check_balance() method
//         print(f'Your transactions {transactions}')

//     elif command == 'exit':
//         break
//     else:
//         print('Command not recognized')