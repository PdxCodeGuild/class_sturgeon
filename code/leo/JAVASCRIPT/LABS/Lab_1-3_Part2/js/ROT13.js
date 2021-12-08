var ROT13 = {
    a : 'n',
    b : 'o',
    c : 'p',
    d : 'q',
    e : 'r',
    f : 's',
    g : 't',
    h : 'u',
    i : 'v',
    j : 'w',
    k : 'x',
    l : 'y',
    m : 'z',
    n : 'a',
    o : 'b',
    p : 'c',
    q : 'd',
    r : 'e',
    s : 'f',
    t : 'g',
    u : 'h',
    v : 'i',
    w : 'j',
    x : 'k',
    y : 'l',
    z : 'm',
    ' ' : ' ',
}

let raw_user_string = document.getElementById("imputROT13")
let submitROT13 = document.getElementById("submitROT13")
let resultsROT13 = document.getElementById('resultsROT13')


submitROT13.addEventListener('click', function() {
    let code = []

    let user_string = raw_user_string.value.toLowerCase() 
    let user_string_list = user_string.split("")
    
    user_string_list.forEach(function(letter) {
        code.push(ROT13[letter])
    })
        let thecode = code.join('')
        resultsROT13.innerText  = (thecode)
})
