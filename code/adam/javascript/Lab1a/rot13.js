var message, message2, rot13, user_input, user_input2
const alpha = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM'


let encryptionButton = document.getElementById("rot13")
let user_encrypt = document.querySelector("#encrypt")
// let user_rot_choice = document.querySelector("#rotnumber")
let encrypt_output = document.getElementById("output")

let decryptionButton = document.getElementById("decryption")
let user_decrypt = document.querySelector("#decrypt")
// let user_rot_choice_decrypt = document.querySelector("#rotnumberdecrypt")
let decrypt_output = document.getElementById("output2")

encryptionButton.onclick=function(){
    message = user_encrypt.value
    // user_input = user_rot_choice.value
    function rot13(message) {
        return message.replace(/[a-z]/gi, letter => alpha[alpha.indexOf(letter) + 13]);
    }
        encrypt_output.innerText=`The cypher for ${message} is: ${rot13(message)}`
}

decryptionButton.onclick=function(){
    message2 = user_decrypt.value
    // user_input2 = user_rot_choice_decrypt.value
    function reverse13(message2) {
        return message2.replace(/[a-z]/gi, letter1 => alpha[alpha.indexOf(letter1) + 13]);
    }
        decrypt_output.innerText=`The decryption for ${message2} is: ${reverse13(message2)}`
}