let ROT13 = {
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

let code = []

let raw_user_string = prompt("Enter a sequence of letters to encode or decode: ")

let user_string = raw_user_string.toLowerCase() 

let user_string_list = user_string.split("")

user_string_list.forEach(function(letter) {
    code.push(ROT13[letter])
})
let thecode = code.join('')

alert(thecode)


 

