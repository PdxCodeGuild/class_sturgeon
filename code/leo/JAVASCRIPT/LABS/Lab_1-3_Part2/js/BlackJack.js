var values = {
    A : 1,
    a : 1,
    J : 10,
    j : 10,
    Q : 10,
    q : 10,
    K : 10,
    k : 10,
    2 : 2,
    3 : 3,
    4 : 4,
    5 : 5,
    6 : 6,
    7 : 7,
    8 : 8,
    9 : 9,
    10 : 10,
}


let card1 = document.getElementById("imputBJ1")
let card2 = document.getElementById("imputBJ2")
let card3 = document.getElementById("imputBJ3")
let submitBJ = document.getElementById("submitBJ")
let resultsBJ = document.getElementById('resultsBJ')


submitBJ.addEventListener('click', function() {
    
    let card1a = parseInt(values[card1.value])
    let card2a = parseInt(values[card2.value])
    let card3a = parseInt(values[card3.value])
    let answer = card1a + card2a + card3a

    if (answer < 17) {
        resultsBJ.innerText = (`${answer} Hit`)
    }
    
    else if (answer >= 17 && answer < 21) {
        resultsBJ.innerText  = (`${answer} Stay`)
    }
    
    else if (answer === 21) {
        resultsBJ.innerText  = (`${answer} BlackJack`)
    }
    
    else if (answer > 21) {
        resultsBJ.innerText  = (`${answer} Already Busted`)
    }

})

