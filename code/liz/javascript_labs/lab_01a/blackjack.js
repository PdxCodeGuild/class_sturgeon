// blackjack advice


function faceCardConverter(cards) {
    let newCards = []
    for (let card of cards) {
        if (['J', 'j', 'Q', 'q', 'K', 'k'].includes(card)) {
            newCards.push(10)
        } else if (card === 'A' || card === 'a') {
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


alert('Your card options are: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K')

let firstCard = prompt('What is your first card? ')
let secondCard = prompt('What is your second card? ')
let thirdCard = prompt('What is your third card? ')

let cards = []
cards.push(firstCard)
cards.push(secondCard)
cards.push(thirdCard)

let cardValues = faceCardConverter(cards)
let advice = blackjackAdvice(cardValues)

alert(advice)