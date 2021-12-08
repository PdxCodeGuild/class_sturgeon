let ONEtoNINE = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

let TENtoNINETEEN = {
    1.0: 'ten',
    1.1: 'eleven',
    1.2: 'twelve',
    1.3: 'thirteen',
    1.4: 'fourteen',
    1.5: 'fifteen',
    1.6: 'sixteen',
    1.7: 'seventeen',
    1.8: 'eighteen',
    1.9: 'nineteen',
}

let TWENTYtoNINETY = {
    2: 'twenty',
    3: 'thirty',
    4: 'fourty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}

let user_choice_of_number = document.getElementById("imputNP")
let submitNP = document.getElementById("submitNP")
let resultsNP = document.getElementById('resultsNP')


submitNP.addEventListener('click', function() {
    
    let a = ""
    let b = ""
    let c = ""
    
    if (user_choice_of_number.value <= 0) {
        resultsNP.innerText  = (`zero`)
    }
    
    else {
     
        let lOOs = Math.floor(user_choice_of_number.value / 100)
        let lOs = Math.floor((user_choice_of_number.value % 100) / 10)
        let TEENS = (user_choice_of_number.value % 100) / 10
        let ls = user_choice_of_number.value % 10
    
        if (lOOs > 0) {
            a = ONEtoNINE[lOOs] + " " + "hundred"
        }
    
        if (lOs > 1.9) {
            b = " " + TWENTYtoNINETY[lOs]
        }
         
        if (TEENS > 0.9 && TEENS < 2) {
            b = " " + TENtoNINETEEN[TEENS]
        }
    
        else if (ls > 0) {
            c = " " + ONEtoNINE[ls]
        }
    
        resultsNP.innerText  = (`${a}${b}${c}`)
    }

})
