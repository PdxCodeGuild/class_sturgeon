//key + value pair object
const cardValues = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

//Creates user hand object
let userHand = []
let userValue = 0

//main function
function playBlackjack(){
    let firstCard = prompt('What is your first card?')
    let secondCard = prompt('What is your second card?')
    let thirdCard = prompt('What is your third card?')

    userHand.push(firstCard)
    userHand.push(secondCard)
    userHand.push(thirdCard)
    
    console.log(userHand)

    for (let each in userHand) {
        if (userHand[each] in cardValues){
            userValue += cardValues[userHand[each]]
        } else {
            alert("Error, one of your inputs was incorrect")
        }
    }

    console.log(userValue)

    if (userValue < 17) {
        document.getElementById('advice').innerHTML = `The total value of your hand is ${userValue}, Hit`
    } else if (userValue >= 17 && userValue < 21) {
        document.getElementById('advice').innerHTML = `The total value of your hand is ${userValue}, Stay`
    } else if (userValue === 21) {
        document.getElementById('advice').innerHTML = `The total value of your hand is ${userValue}, Blackjack!`
    } else {
        document.getElementById('advice').innerHTML = `The total value of your hand is ${userValue}, Already Busted`
    }
}