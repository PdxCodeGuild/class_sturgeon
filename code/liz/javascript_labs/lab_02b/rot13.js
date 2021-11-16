// ROT Cipher

function rotCipher(rotation, str) {
    let abcArr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    str = str.split('')
    let newWord = ''
    for (let i of str) {
        let newIndex = abcArr.indexOf(i) + rotation
        if (newIndex >= 26) {
            newIndex -= 26
        }
        newWord += abcArr[newIndex]
    }
    return newWord
}

// let userStr = prompt('What word would you like to encrypt? ')

// let rot = prompt('How much rotation would you like to use? ')


// alert(rotCipher(parseInt(rot), userStr))

let button = document.getElementById("encrypt")
button.addEventListener('click', function() {
    let rot = document.getElementById("rot")
    let input = document.getElementById("input-word")
    let encryption = rotCipher(parseInt(rot.value), (input.value))
    let output = document.getElementById("encrypted-text")
    output.innerText = `${encryption}`
})