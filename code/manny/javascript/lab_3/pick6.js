
// Create empty array for winning ticket
let winningTicket = [];
let ticketsBought = [];
// creates the winning ticket by adding six random number
var i = 6; 
while(i>0){
    let randomDigit = Math.floor(Math.random() * (99 - 1 + 1) +1);
    winningTicket.push(randomDigit);
    i--;
}
// prints the winning ticket on html
document.getElementById('winner').innerHTML = winningTicket.sort()
// I have to get the number of tickets bought, check them with winning numbers, then measure how much money the customer won

function numberOfTickets(){
    console.log("this works")
}