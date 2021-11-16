class ATM {
    constructor(balance=0, interest=0.001, history = []) {
        this.balance = balance
        this.interest = interest
        this.history = history
    }
    get_balance() {
        return parseFloat(this.balance).toFixed(2)
    }
    deposit(amount) {
        // this.balance = parseFloat(this.balance)
        // amount = parseFloat(amount)
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
let screen_balance = document.querySelector("#screen_balance")
let screen_history = document.querySelector("#screen_history")
let interest
let round_interest


let deposit_bt = document.querySelector("#deposit_bt")
deposit_bt.addEventListener("click", function () {
    amount = document.querySelector("#num")
    let cash_in = parseFloat(amount.value)
    screen_balance.innerText = `Balance: $${atm.deposit(cash_in)}`
    screen_history.innerText = atm.history.reverse().join("\n")
})

let withdraw_bt = document.querySelector("#withdraw_bt")
withdraw_bt.addEventListener("click", function () {
    amount = document.querySelector("#num")
    let cash_out = parseFloat(amount.value)
    screen_balance.innerText = `Balance: $${atm.withdraw(cash_out)}`
    screen_history.innerText = atm.history.reverse().join("\n")
})

let interest_bt = document.querySelector("#interest_bt")
interest_bt.addEventListener("click", function () {
    interest = atm.calc_interest()
    round_interest = parseFloat(interest.toFixed(2))
    atm.history.push(`Accumulated $${round_interest} in interest`)
    screen_balance.innerText = `Balance: $${atm.deposit(round_interest)}`
    screen_history.innerText = atm.history.reverse().join("\n")
})