// blackjack advice


function faceCardConverter(cards) {
    let newCards = []
    for (let card of cards) {
        if (['J', 'Q', 'K'].includes(card)) {
            newCards.push(10)
        } else if (card === 'A') {
            newCards.push(1)
        } else {
            newCards.push(parseInt(card))
        }
    }
    return newCards
}


function blackjackAdvice(cards) {
    let cardsSum = 0
    for (let card of cards) {
        cardsSum += card
    }
    if (cardsSum < 17) {
        return `${cardsSum} Hit`
    } else if (cardsSum >= 17 && cardsSum < 21) {
        return `${cardsSum} Stay`
    } else if (cardsSum === 21) {
        return `${cardsSum} Blackjack!`
    } else {
        return `${cardsSum} Already Busted`
    }
}


// userInput
let firstCard = document.getElementById('card1')
let secondCard = document.getElementById('card2')
let thirdCard = document.getElementById('card3')


let cards = []
cards.push(firstCard.value)
cards.push(secondCard.value)
cards.push(thirdCard.value)

let cardValues = faceCardConverter(cards)
let advice = blackjackAdvice(cardValues)

// advice event
let button = document.getElementById("get-advice")
button.addEventListener('click', function() {
    let output = document.getElementById("advice-text")
    output.innerText = `${advice}`
})
