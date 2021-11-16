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
        return `Sum: ${cardsSum}\n\nAdvice: Hit`
    } else if (cardsSum >= 17 && cardsSum < 21) {
        return `Sum: ${cardsSum}\n\nAdvice: Stay`
    } else if (cardsSum === 21) {
        return `Sum: ${cardsSum}\n\nAdvice: Blackjack!`
    } else {
        return `Sum: ${cardsSum}\n\nAdvice: Already Busted`
    }
}


function addToArray(card1, card2, card3) {
    let cards = []
    cards.push(card1.value)
    cards.push(card2.value)
    cards.push(card3.value)
    console.log(cards)
    return cards
}

// userInput

let firstCard = document.getElementById('card1')
let secondCard = document.getElementById('card2')
let thirdCard = document.getElementById('card3')


// advice event
let button = document.getElementById("get-advice")
button.addEventListener('click', function() {
    let cards = addToArray(firstCard, secondCard, thirdCard)
    let cardValues = faceCardConverter(cards)
    let advice = blackjackAdvice(cardValues)
    let output = document.getElementById("advice-text")
    output.innerText = `${advice}`
})
