// pick 6

function pick6() {
    let numList = []
    while (numList.length < 6) {
        numList.push(Math.floor(1 + Math.random()*99))
    }
    return numList
}

function numMatches(winning, ticket) {
    let matches = 0
    for (let i = 0; i < winning.length; i++) {
        if (winning[i] === ticket[i]) {
            matches += 1
        }
    }
    return matches
}

function winnings (matches) {
    if (matches === 1) {
        return 4
    } else if (matches === 2) {
        return 7
    } else if (matches === 3) {
        return 100
    } else if (matches === 4) {
        return 50000
    } else if (matches === 5) {
        return 1000000
    } else if (matches === 6) {
        return 25000000
    } else {
        return 0
    }
}


function generateTickets (numTickets) {
    let totalWinnings = 0
    let ticketCost = 0

    let winningTicket = pick6()

    let x = 0
    while (x < numTickets) {
        x++
        let ticket = pick6()
        let matches = numMatches(winningTicket, ticket)
        totalWinnings += winnings(matches)
        ticketCost += 2
    }

    let finalBalance = totalWinnings - ticketCost
    let roi = finalBalance / ticketCost
    return `You won $${totalWinnings} and spent $${ticketCost} on Pick6.\nYour final balance is $${finalBalance}.\nYour return on investment is ${roi}%`
}


let numTickets = document.getElementById("amount")
let button = document.getElementById("results")
button.addEventListener('click', function() {
    let results = generateTickets(parseInt(numTickets.value))
    let output = document.getElementById("results-text")
    output.innerText = `${results}`
})

