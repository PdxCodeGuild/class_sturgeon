class ATM {
    constructor(balance=0, interest=0.001, history = []) {
        this.balance = balance
        this.interest = interest
        this.history = history
    }
    get_balance() {
        return this.balance
    }
    deposit(amount) {
        this.balance += amount
        this.history.push(`User deposited $${amount}`)
        return this.get_balance()
    }
    check_with(amount) {
        if (amount <= this.get_balance()) {
            return true
        } else return false
    }
    withdraw(amount) {
        this.balance -= amount
        this.history.push(`User withdrew $${amount}`)
        return this.get_balance()        
    }
    calc_interest() {
        let int
        int = this.balance * this.interest
        return int
    }
    
}

let atm = new ATM()



// alert(parseInt(amount)+5)

// let amount = prompt("How Much?")

// if (atm.check_with(amount)) {
//     alert(`balance is now ${atm.withdraw(amount)}`)
// } else alert(`${amount} is more than your balance of ${atm.get_balance()}`)
let command


alert("Welcome to the ATM!")
while (true) {
    
    command = prompt("Enter command:\nBalance\nDeposit\nWithdraw\nInterest\nHistory\nExit")
    if (command === 'balance') {
        alert("$" + atm.get_balance())
    }
    else if (command === 'deposit') {
        amount = parseFloat(prompt("How much to deposit?"))
        alert(`Balance: $${atm.deposit(amount)}`)
    }
    else if (command === 'withdraw') {
        amount = parseFloat(prompt("How much to withdraw?"))
        if (atm.check_with(amount)) {
            alert(`New balance: $${atm.withdraw(amount)}`)
        } else {
            alert(`$${amount} is more than your balance of $${atm.get_balance()}`)
        }
    }
    else if (command === 'history') {
        alert(atm.history.join("\r\n"))
    }
    else if (command === 'interest') {
        amount = atm.calc_interest()
        atm.deposit(amount)
        alert(`Accumulated $${amount} in interest`)
    }
    else if (command === 'exit') {
        alert("Goodbye!")
        break
    }
    else {
        prompt("Command not recognized, try again..")
    }
}