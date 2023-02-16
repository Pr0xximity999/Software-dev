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

//Addition
var h1 = document.createElement('h1');
h1.innerHTML = 'Optellen van 2 arrays zijn:'
document.getElementById('body').appendChild(h1);
for (let i = 0; i < arrayEen.length; i++){
    var p = document.createElement("p");
    p.innerHTML = optellen(arrayEen[i], arrayTwee[i]);
    document.getElementById('body').appendChild(p);
}

//Subtraction
var h1 = document.createElement('h1'); 
h1.innerHTML = 'Aftrekken van 2 arrays zijn:';
document.getElementById('body').appendChild(h1);
for (let i = 0; i < arrayEen.length; i++){
    var p = document.createElement("p");
    p.innerHTML = aftrekken(arrayEen[i], arrayTwee[i]);
    document.getElementById('body').appendChild(p);
}

//Multiplication
var h1 = document.createElement('h1'); 
h1.innerHTML = 'Vermenigvuldigen van 2 arrays zijn:';
document.getElementById('body').appendChild(h1);
for (let i = 0; i < arrayEen.length; i++){
    var p = document.createElement("p");
    p.innerHTML = vermenigvuldien(arrayEen[i], arrayTwee[i]);
    document.getElementById('body').appendChild(p);
}

//Division
var h1 = document.createElement('h1'); 
h1.innerHTML = 'Delen van 2 arrays zijn:';
document.getElementById('body').appendChild(h1);
for (let i = 0; i < arrayEen.length; i++){
    var p = document.createElement("p");
    p.innerHTML = delen(arrayEen[i], arrayTwee[i]);
    document.getElementById('body').appendChild(p);
}

