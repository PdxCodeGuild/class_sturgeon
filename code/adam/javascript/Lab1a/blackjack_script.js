var age, approved_list, card1, card2, card3

let bjoutput = document.getElementById("output")
let blackJackButton = document.getElementById("BJ")

blackJackButton.onclick=function(){

age = prompt("Are you at least 21 years of age? (y/n)").toLowerCase()
if ((age == 'y') || (age == 'yes')) {
    // document.write("Welcome to the BlackJack Advisor")

    player_card1 = prompt("What is your first card?-->").toUpperCase()
    player_card2 = prompt("What is your second card?-->").toUpperCase()
    player_card3 = prompt("What is your third card?-->").toUpperCase()

    function blackJack(card1, card2, card3) {
        let final_amount = 0;
        // card 1 value
        if ((card1 == "J") || (card1 == "Q") || (card1 == "K")) {
            final_amount += 10;
        } else if (card1 == "A") {
            final_amount += 1;
        } else {
            final_amount += parseInt(card1)
        }
        // card 2 value
        if ((card2 == "J") || (card2 == "Q") || (card2 == "K")) {
            final_amount += 10;
        } else if (card2 == "A") {
            if (final_amount >= 10) { 
                final_amount += 1;
            } else final_amount += 11;
        } else {
            final_amount += parseInt(card2)
        }
        // card 3 value
        if ((card3 == "J") || (card3 == "Q") || (card3 == "K")) {
            final_amount += 10;
        } else if (card3 == "A") {
            if (final_amount >= 10) { 
                final_amount += 1;
            } else final_amount += 11;
        } else {
            final_amount += parseInt(card3)
        }
        // time to do an ace check on card 1
        if ((final_amount <=10) && (card1 == "A")) {
            final_amount += 10
        }
        // Determining soft hit below 17, stay 17-21, win at 21, and busted over 21  
        if (final_amount < 17) {
            bjoutput.innerText=`You have a score of ${final_amount}. You are under 17, Hit!`
        } if ((final_amount >= 17) && (final_amount < 21)) {
            bjoutput.innerText=`You have a score of ${final_amount}. Between 17 and 21 = danger zone, STAY!`
        } if (final_amount == 21) {
            bjoutput.innerText=`You have a score of ${final_amount}. Blackjack! (don't hit, you won!)`
        } if (final_amount > 21) {
            bjoutput.innerText=`You have a score of ${final_amount}. Already Busted, choose smaller cards next time.`
        }
    }
    approved_list = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

    blackJack(player_card1, player_card2, player_card3)

} else {
    bjoutput.innerText="Too bad! Gambling is for those over the age of 21, please wait until you are older."
}
}