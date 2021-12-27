const password = document.querySelector('#password');
const button = document.querySelector('#button');

let chars = 'abcdefghijklmnop123456789ABCDEFGHIJKLMNOPQ!@#$%';
let length = 10;
let passwordValue = '';

const createPassword = () => {
    passwordValue = '';
    for (let i=0; i < length; i++) {
        let number = Math.floor(Math.random()* chars.length);
        passwordValue += chars.substring(number, number + 1)
    }

    password.value = passwordValue;
};

button.addEventListener('click', createPassword)