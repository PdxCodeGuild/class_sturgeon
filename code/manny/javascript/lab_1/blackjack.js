//key/value pair object
const cardValues = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

//ask for card values
function question(){
    let totalValue = 0 
    var cardOne = prompt("What's the first card that you drew?", "Enter card ");
    var cardTwo = prompt("What's the second card?", "Enter 2nd card");
    var cardThree = prompt("What's the third card?", "Enter 3rd card here");
    
    //math stuff
    totalValue += cardValues[cardOne] + cardValues[cardTwo] + cardValues[cardThree]
    //outputs suggestings t
    
    if (totalValue < 21){
        alert(totalValue + "Hit!! You have a chance to win!")
    }
    if (totalValue = 21){
        alert(totalValue + "Stay you have Blackjack!")
    }
    if (totalValue > 21) {
        alert(totalValue + "Bust, you're too good at this game.")
    }
}