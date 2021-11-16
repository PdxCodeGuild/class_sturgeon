var amount, atm, atmChoices, balance, depositAmount, extra, interest, log_rows, pin, transactions, withdrawlAmount, yesOrNo


    class ATM {
        constructor(balance=100) {
            this.balance = balance
            this.interest = .001
            this.transactions = []
        }
        check_balance() {
            document.getElementById ('atm_response_area').innerHTML =`You balance is $${this.balance}`
            extra = (this.balance * this.interest).toFixed(2)
        }
        deposit() {
            depositAmount = document.getElementById ("myselect1").value;
            depositAmount = parseInt(depositAmount)
            if (depositAmount !== "" && depositAmount !== null && !isNaN(depositAmount)) {
                this.balance += depositAmount;
                document.getElementById ('atm_response_area').innerHTML =`You have successfully deposited $${depositAmount}. You know have $${this.balance}`
            } else {
                alert("Error: please enter a number!");
                atm.deposit();
            }
        }
        withdrawl() {
            withdrawlAmount = document.getElementById ('withdrawl').value;
            withdrawlAmount = parseInt(withdrawlAmount)
            if (withdrawlAmount !== "" && withdrawlAmount !== null && !isNaN(withdrawlAmount)) {
                if (withdrawlAmount >= 20) {
                    if (withdrawlAmount <= this.balance) {
                        this.balance -= withdrawlAmount;
                        document.getElementById ('withdraw_option').innerHTML =`Your withdrawl amount is $${withdrawlAmount}, Your remaining balance is $${this.balance}`
                    } else {
                        alert("You do not have sufficient funds!");
                        atm.withdrawl();
                    }
                } else {
                    alert("You must withdraw at least $20");
                    atm.withdrawl();
                }
            } else {
                alert("Error: please enter a number!");
                atm.withdrawl();
            }
        }
    }

    atm = new ATM()

    function getaction(){
        var pin = document.getElementById ('pin').value;
        //To check Pin entered is correct or not
        if(pin=='1234'){
            document.getElementById("password_success_text_area").innerHTML ="Please Choose transcation";
            document.getElementById('radio_options'). style.display = 'block'; 
            } else {
                document.getElementById ("password_success_text_area").innerHTML = "Invalid pin";
            }
        }
        
        
        function myfunction(val){
        if(val==1) {
            document.getElementById ('check_balance').style.display = 'block';
            document.getElementById ('withdraw_option' ). style.display = 'none';
            document.getElementById ('deposit_option' ). style.display = 'none';
        } else if(val==2) {
            document.getElementById ('check_balance').style.display = 'none';
            document.getElementById ('withdraw_option').style.display = 'block';
            document.getElementById ('deposit_option').style.display = 'none';
        } else if(val==3) {
            document.getElementById ('check_balance').style.display = 'none';
            document.getElementById ('deposit_option').style.display = 'block';
            document.getElementById ('withdraw_option').style.display = 'none';
        }
        }