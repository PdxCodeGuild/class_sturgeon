// ROT Cipher

function rotCipher(rotation, userStr) {
    let abcArr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']

    let userStr = userStr.split('')
    let newWord = ''
    for (let i of userStr) {
        let newIndex = abcArr.indexOf(i) + rotation
        if (newIndex >= 26) {
            newIndex -= 26
        }
        newWord += abcArr[newIndex]
    }
    return newWord
}


let rot = prompt('How much rotation would you like to use? ')

userStr = prompt('What word would you like to encrypt? ')
encrypted = rotCipher(parseInt(rot), userStr)
alert(encrypted)