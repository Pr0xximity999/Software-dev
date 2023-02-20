var len = prompt('Voer een getal in')
len++
var p = document.createElement("p");
p.innerHTML = `Array: ${[...Array(len).keys()]}`;
document.getElementById('body').appendChild(p);
var numbers = []
for (let i = 0; i < len; i++) {
    numbers.push(i)
    var p = document.createElement("p");
    p.innerHTML = numbers.join('');
    document.getElementById('body').appendChild(p);
}



