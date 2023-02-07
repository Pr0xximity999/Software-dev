//List for the number sequence
var sequence = [1, 1]
var numbers = 20

//Function for adding numbers
function addition(num1, num2){
    return num1 + num2
}

//Looping 20 times to get 20 numbers of the fibbionachi sequence
for(let i = 0; i < numbers; i++){
    sequence.push(addition(sequence[sequence.length - 1], sequence[sequence.length - 2]))
}

document.getElementById('text').innerHTML = sequence;

