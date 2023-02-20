var len = prompt('Voer een getal in')
len++
var p = document.createElement("p");
p.innerHTML = `Array: ${[...Array(len).keys()]}`;
document.getElementById('body').appendChild(p);

for (let i = len; i > 0; i--) {
    var p = document.createElement("p");
    p.innerHTML = [...Array(i).keys()].join('');
    document.getElementById('body').appendChild(p);
}



