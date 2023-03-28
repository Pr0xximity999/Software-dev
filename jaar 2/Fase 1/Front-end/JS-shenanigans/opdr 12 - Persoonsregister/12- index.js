const data = {
    "voornaam": "Piet",
    "achternaam": "Heijn",
    "nationaliteit": "Nederlandse",
    "leeftijd": 47,
    "gewicht": 86
 }
var body = document.getElementById('body')
 for (const [key, value] of Object.entries(data)) {
    var p = document.createElement('p')
    p.innerHTML = `${key}: ${value}`
    body.appendChild(p)
    
}