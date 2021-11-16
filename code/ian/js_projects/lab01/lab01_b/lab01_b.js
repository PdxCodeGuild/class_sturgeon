8 
let card_values1 = {
    'a': 11,
    'A': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'j': 10,
    'J': 10,
    'q': 10,
    'Q': 10,
    'k': 10,
    'K': 10
}
let card_values2 = {
    'a': 1,
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'j': 10,
    'J': 10,
    'q': 10,
    'Q': 10,
    'k': 10,
    'K': 10
}
let c1 = document.querySelector("#c1")
let c2 = document.querySelector("#c2")
let c3 = document.querySelector("#c3")
let total
let total2

let bt = document.querySelector("#bt")
bt.addEventListener("click", function () {
    let score = document.querySelector("#score")

    total = card_values1[c1.value] + card_values1[c2.value] + card_values1[c3.value]

    if (total < 17) {

        score.innerText = `You should hit at ${total}`

    }
    else if (17 <= total && total < 21) {
        score.innerText = `You should stay at ${total}`
    }
    else if (total === 21) {
        score.innerText = `${total} BLACKJACK`
    }
    else if (total > 21) {
        total = card_values2[c1.value] + card_values2[c2.value] + card_values2[c3.value]

        if (total < 17) {
            score.innerText = `You should hit at ${total}`
        }
        else if (17 <= total && total < 21) {
            score.innerText = `You should stay at ${total}`
        }
        else if (total === 21) {
            score.innerText = `${total} BLACKJACK`
        }
        else if (total > 21) {
            score.innerText = `${total} BUSTED`
        }
    }


})

