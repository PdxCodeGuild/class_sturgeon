let alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');

var cryptex = []
var rotation = 13 //just in case we want the user to pick rotation
 
function encrypt(){
  let userInput = document.getElementById("userInput").value; 
  
  userInput =  userInput.split('')

  for (let i of userInput){
    if (alphabet.includes(i)){
      let newCryptoid = alphabet.indexOf(i)
      if (newCryptoid < rotation){
        newCryptoid += 13;
        cryptex.push(newCryptoid)
      } else {
        newCryptoid -= 13;
        cryptex.push(newCryptoid)
      }
    }
  }
  let results = []
  
  for (let j of cryptex){
    results.push(alphabet[j].toString())
  }
  results = results.join('')
  document.getElementById('answer').innerHTML = `Your encrypted word is ${results}`;
}