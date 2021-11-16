var card1, card2, card3, player_choice1, player_choice2, player_choice3

let bjoutput = document.getElementById("bjoutput")

let big_button = document.querySelector("#big_button")

let cards = document.getElementsByClassName("cards")
for (let i=0; i<cards.length; i++) {
    cards[i].addEventListener("click", function(){
        player_choice1 = cards[i].id
        for (let i=0; i<cards.length; i++) {
            if (cards[i].classList.contains('active-card')){
                cards[i].classList.remove('active-card')
            }
        }
        cards[i].classList.add('active-card')
        console.log(`player choice 1: ${player_choice1}`)
    })
}

let cards2 = document.getElementsByClassName("cards2")
for (let i=0; i<cards2.length; i++) {
    cards2[i].addEventListener("click", function(){
        player_choice2 = cards2[i].id
        for (let i=0; i<cards2.length; i++) {
            if (cards2[i].classList.contains('active-card')){
                cards2[i].classList.remove('active-card')
            }
        }
        cards2[i].classList.add('active-card')
        console.log(`player choice 2: ${player_choice2}`)
    })
}

let cards3 = document.getElementsByClassName("cards3")
for (let i=0; i<cards3.length; i++) {
    cards3[i].addEventListener("click", function(){
        player_choice3 = cards3[i].id
        for (let i=0; i<cards3.length; i++) {
            if (cards3[i].classList.contains('active-card')){
                cards3[i].classList.remove('active-card')
            }
        }
        cards3[i].classList.add('active-card')
        console.log(`player choice 3: ${player_choice3}`)
    })
}

big_button.onclick = function() {
    let player_card1 = player_choice1
    let player_card2 = player_choice2
    let player_card3 = player_choice3

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
            final_amount += 1;
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
        if ((final_amount <=10) && (card2 == "A")) {
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

    blackJack(player_card1, player_card2, player_card3)
}