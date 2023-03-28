var arrayEen = [1,2,3,4,5,6,7,8,9,10];
var arrayTwee = [2,4,6,8,10,12,14,16,18,20];

function optellen(num1, num2){
    return `${num1} + ${num2} = ${num1 + num2}`
}
function aftrekken(num1, num2){
    return `${num2} - ${num1} = ${num2 - num1}`
}
function vermenigvuldien(num1, num2){
    return `${num1} * ${num2} = ${num1 * num2}`
}
function delen(num1, num2){
    return `${num2} / ${num1} = ${num2 / num1}`
}

function bereken(text, func){
    var h1 = document.createElement('h1');
    h1.innerHTML = text
    document.getElementById('body').appendChild(h1);
    for (let i = 0; i < arrayEen.length; i++){
        var p = document.createElement("p");
        p.innerHTML = func(arrayEen[i], arrayTwee[i]);
        document.getElementById('body').appendChild(p);
    }
}

//Addition
bereken('Optellen van 2 arrays zijn:', optellen)

//Subtraction
bereken('Aftrekken van 2 arrays zijn:', aftrekken)


//Multiplication
bereken('Vermenigvuldigen van 2 arrays zijn:', vermenigvuldien)

//Division
bereken('Delen van 2 arrays zijn:', delen)

