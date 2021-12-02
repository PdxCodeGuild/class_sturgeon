
function randint(a, b) {
    return Math.floor(a + Math.random()*b)
}

function pick6(arr) {
    while (arr.length < 6)
        arr.push(randint(1,99))
    return arr
}

function num_matches (win, tic) {
    let matches=0
    for (let i=0; i<win.length; i++) {        
        if (win[i] === tic[i]) {
            matches ++
        }
    } return matches
}


winning_nums = []
pick6(winning_nums)

let pot_earnings = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000
 
}

let balance = 0
let counter = 0 
let ticket
let act_earnings =0
let expenses =0


while (counter < 100000) {
    ticket = []
    counter ++
    balance -= 2
    matches = 0
    expenses += 2
    
    pick6(ticket)
    balance += pot_earnings[num_matches(winning_nums, ticket)]
    act_earnings += pot_earnings[num_matches(winning_nums, ticket)]
}
alert(`balance ${balance}`)

alert("ROI: " + (act_earnings-expenses)/expenses)