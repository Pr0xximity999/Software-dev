var getallen = [2, 4, 6, 8]

var arrayEen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

function vermenigvuldien(num1, num2) {
    return `${num1} * ${num2} = ${num1 * num2}`
}

for (let z = 0; z < getallen.length; z++) {
    var h1 = document.createElement('h1');
    h1.innerHTML = `Tafel van ${getallen[z]}`
    document.getElementById('body').appendChild(h1);
    for (let i = 0; i < arrayEen.length; i++) {
        var p = document.createElement("p");
        p.innerHTML = vermenigvuldien(arrayEen[i], getallen[z]);
        document.getElementById('body').appendChild(p);
    }
}


