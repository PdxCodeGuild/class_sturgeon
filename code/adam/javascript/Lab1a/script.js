var amount, atm, atmChoices, balance, depositAmount, extra, interest, log_rows, pin, transactions, withdrawlAmount
pin = prompt("Welcome to the ATM, What is your pin?")
if (pin == '1234') {
    // setTimeout(() => { alert("Password Accepted"); }, 10)

    class ATM {
        constructor(balance=0) {
            this.balance = balance
            this.interest = .001
            this.transactions = []
        }
        check_balance() {
            alert(`Your current balance is $${this.balance}`)
            extra = (this.balance * this.interest).toFixed(2)
            this.transactions.push(`User checked account interest of $${extra}`)
            toContinue();
        }
        deposit() {
            depositAmount = parseInt(prompt("Enter amount to deposit: "));
            if (depositAmount !== "" && depositAmount !== null && !isNaN(depositAmount)) {
                this.balance += depositAmount;
                this.transactions.push(`User deposited $${depositAmount}`);
                alert(`You have successfully deposited $${depositAmount}. You know have $${this.balance}`);
                toContinue();
            } else {
                alert("Error: please enter a number!");
                deposit();
            }
        }
        withdrawl() {
            withdrawlAmount = parseInt(prompt(`How much do you wish to withdraw? \n The minimum amount is $20`));
            if (withdrawlAmount !== "" && withdrawlAmount !== null && !isNaN(withdrawlAmount)) {
                if (withdrawlAmount >= 20) {
                    if (withdrawlAmount <= this.balance) {
                        this.balance -= withdrawlAmount;
                        alert("Transaction successful!");
                        alert(`Your remaining balance is $${this.balance}`);
                        toContinue();
                    } else {
                        alert("You do not have sufficient funds!");
                        withdrawal();
                    }
                } else {
                    alert("You must withdraw at least $20");
                    withdrawal();
                }
            } else {
                alert("Error: please enter a number!");
                withdrawal();
            }
        }
        print_transactions() {
            print("")
            print("User log at ATM:")
            log_rows = '\n'.join(this.transactions)
            print(log_rows)
        }
        toContinue() {
            var yesOrNo = parseInt(prompt("Do you want to perform another transaction? \n 1. Yes \n 2. No"));
            if (yesOrNo !== "" && yesOrNo !== null) {
                if (yesOrNo === 2){
                    exit();
                }
                else {
                    selectAccountType(); 
                }
            } else {
                alert("Please make a valid selection");
                toContinue();
            }
        }
        exit() {
            alert("Thank you for patronising our ATM machine");
        }
    }

    atm = new ATM()
    console.log(atm)
    function doSomething() {
        console.log(atm)
        atmChoices = parseInt(prompt("what can we do for you today? \n 1. Check Balance \n 2. Withdrawal \n 3. Deposit \n 4. Exit"));
        if (atmChoices !== "" && atmChoices !== null && !isNaN(atmChoices)) {
            switch (atmChoices) {
                case 1:
                    atm.check_balance();
                    console.log("check balance")
                    break;
                case 2:
                    atm.withdrawl();
                    break;
                case 3:
                    atm.deposit();
                    break;
                case 4:
                    atm.exit();
                    break;
                default:
                    alert('Please make a valid selection');
                    doSomething();
            }
        } else {
            alert("Please make a valid selection");
            doSomething()
        }
    }
    
    document.write("<h1>asynchronous coding")

    doSomething()

} else {
    setTimeout(() => { alert("Wrong Answer!"); }, 1000)
    temp = document.write("")
} 

