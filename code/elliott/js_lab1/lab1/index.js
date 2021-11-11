
var winList = []
while (winList.length != 6) {
    winList.push(Math.floor(Math.random() * 100))
}

var tickBalance = 0
var winnings = 0
var tickets = 0

while (tickets < 100) {
    tickets++
    tickBalance += 2
    console.log('new ticket made')

    let userList = []
    while(userList.length != 6) {
        userList.push(Math.floor(Math.random() * 100))
    } 
    
    let userMatches = 0
    console.log(winList)
    console.log(userList)
    if (userList[0] === winList[0]) {
        userMatches += 1
    }
    if (userList[1] === winList[1]) {
        userMatches += 1
    }
    if (userList[2] === winList[2]) {
        userMatches += 1
    }
    if (userList[3] === winList[3]) {
        userMatches += 1
    }
    if (userList[4] === winList[4]) {
        userMatches += 1
    }
    if (userList[5] === winList[5]) { 
        userMatches += 1
    }


    if (userMatches === 1) {
        winnings += 4
    }
    else if (userMatches === 2) {
        winnings += 7
    }
    else if (userMatches === 3) {
        winnings += 100
    }
    else if (userMatches === 4) {
        winnings += 50000
    }
    else if (userMatches === 5) {
        winnings += 100000
    }
    else if (userMatches === 6) {
        winnings += 250000
    }
}

x = `Your winnings are, ${winnings}. Your ticket balance is ${tickBalance}`
alert(x)
