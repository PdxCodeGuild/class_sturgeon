
let card_values1 = {
    'a' : 11,
    'A' : 11,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'j' : 10,
    'J' : 10,
    'q' : 10,
    'Q' : 10,
    'k' : 10,
    'K' : 10
}
let card_values2 = {
    'a' : 1,
    'A' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'j' : 10,
    'J' : 10,
    'q' : 10,
    'Q' : 10,
    'k' : 10,
    'K' : 10
}

let card1 = prompt("What is your 1st card?")
let card2 = prompt("What is your 2nd card?")
let card3 = prompt("What is your 3rd card?")
let total = card_values1[card1] + card_values1[card2] + card_values1[card3]

if (total < 17) {
    alert("You should hit at " + total)
} else if (17 <= total && total < 21) {
    alert("You should stay at " + total)
} else if (total === 21) {
    alert(total + " BLACKJACK!")
} else if ( total > 21) {
    total = card_values2[card1]+card_values2[card2]+card_values2[card3]
} if (total < 17) {
    alert("You should hit at " + total)
} else if (17 <= total && total < 21) {
    alert("You should stay at " + total) 
} else if (total === 21) {
    alert (total + " BLACKJACK!!")
} else if (total > 21) {
    alert(total + " BUSTED!!")
}
