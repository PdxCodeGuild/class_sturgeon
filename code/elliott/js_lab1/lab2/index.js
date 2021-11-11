
let outputField = document.getElementById('something')
let encriptionOutput = document.getElementById('something1')




userInput = prompt('Enter in your characters!');

let encriptionList = userInput;

const coder = {
    'a': "n", 'b': "o", 'c': "p", 'd': "q", 'e': "r", 'f': "s", 'g': "t", 'h':  "u",
    'i': "v", 'j': "w", 'k': "x", 'l': "y", 'm': "z", 'n': "a", 'o': "b", 'p': "c",
    'q': "d", 'r': "e", 's':  "f", 't': "g", 'u': "h", 'v': "i", 'w': "j", 'x': "k",
    'y': "l", 'z': "m"
}

let encription = [];

for (let list of encriptionList) {
    encription.push(coder[list])
}

//alert(`This is your encripted message: ${encription}`)

secondInput = prompt('Enter your encripted message to do your original message.')

let deList = secondInput;

let decription = []
for ( let list of deList) {
    decription.push(coder[list])
}

//alert(`Your decripted message is: ${decription}`)

encriptionOutput.innerText = `This is your encripted message: ${encription}`
outputField.innerText = `Your decripted message is: ${decription}`