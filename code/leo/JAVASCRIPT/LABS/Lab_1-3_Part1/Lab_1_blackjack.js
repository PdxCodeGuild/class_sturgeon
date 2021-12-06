
let values = {
    A : 1,
    a : 1,
    J : 10,
    j : 10,
    Q : 10,
    q : 10,
    K : 10,
    k : 10,
    2 : 2,
    3 : 3,
    4 : 4,
    5 : 5,
    6 : 6,
    7 : 7,
    8 : 8,
    9 : 9,
    10 : 10,
}

let card1 = prompt("What's your firt card? ")
let card1a = parseInt(values[card1])

let card2 = prompt("What's your second card? ")
let card2a = parseInt(values[card2])

let card3 = prompt("What's your third card? ")
let card3a = parseInt(values[card3])

let answer = card1a + card2a + card3a

if (answer < 17) {
    alert(`${answer} Hit`)
}

else if (answer >= 17 && answer < 21) {
    alert(`${answer} Stay`)
}

else if (answer === 21) {
    alert(`${answer} BlackJack`)
}

else if (answer > 21) {
    alert(`${answer} Already Busted`)
}
