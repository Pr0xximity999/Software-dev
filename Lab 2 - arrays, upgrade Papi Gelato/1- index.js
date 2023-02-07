
var weekdagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]

document.getElementById('weekdagen').innerHTML = weekdagen;
document.getElementById('werkdagen').innerHTML = weekdagen.slice(0, 4);
document.getElementById('weekenddagen').innerHTML = weekdagen.slice(5, 6);
document.getElementById('omgekeerd').innerHTML = weekdagen.slice(0, 4).reverse() ;
document.getElementById('omgekeerdweekend').innerHTML = weekdagen.slice(5, 6).reverse();

