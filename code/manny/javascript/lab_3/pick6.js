
// Create empty array for winning ticket
var winningTicket = [];
var tickets = [];
var rewards = {
    1 : 4, 2 : 7, 3 : 100, 4 : 50000, 5 : 1000000, 6 : 25000000  
} 

// creates the winning ticket by adding six random number

function createWinner(){
    let i = 6; 
    while ( i>0 ){
        let randomDigit = Math.floor(Math.random() * (99 - 1 + 1) +1); winningTicket.push(randomDigit); i--;
    }
    
    winningTicket = winningTicket.sort(function(a,b){
        return a-b; 
    });

    document.getElementById('winner').innerHTML = `The Winning Numbers are: ${winningTicket}`
    
    console.log(winningTicket)
}

// check them with winning numbers, then measure how much money the customer won

function numberOfTickets(){
    var ticketsBought = document.getElementById('amountBought').value;
    
    document.getElementById('results').innerHTML = `You have purchased ${ticketsBought} lottery tickets.`;
    
    for (let j = ticketsBought; j > 0; j--){
        let bought = []
        for (let i = 6; i > 0; i--){
            let randomDigit = Math.floor(Math.random() * (99 - 1 + 1) +1); 
            bought.push(randomDigit);
        }
        bought = bought.sort(function(a,b){
            return a-b; 
        });
        tickets.push(bought)
    }
    console.log(tickets)

    let numOfMatches = []
    let totalPurse = 0 
    totalPurse -= ticketsBought
    
    tickets.forEach(function(each){
        count = 0
        each.forEach(function(matcher){
            if (winningTicket.includes(matcher)){
                count += 1
            }
        })
        numOfMatches.push(count) 
    })
    console.log(numOfMatches)

    numOfMatches.forEach(function(each){
        if (numOfMatches[each] in rewards){
            totalPurse += rewards[numOfMatches[each]]
        }
    })
    console.log(totalPurse)

    document.getElementById('money').innerHTML = `You've made ${totalPurse} dollars!`;
}
