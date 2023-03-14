//The user data
data = [{
   "voornaam": "Piet",
   "achternaam": "Heijn",
   "nationaliteit": "Nederlandse",
   "leeftijd": 47,
   "gewicht": 86
},
{
   "voornaam": "Masud",
   "achternaam": "Mohammed",
   "nationaliteit": "Iraans",
   "leeftijd": 37,
   "gewicht": 79
},
{
   "voornaam": "Marie",
   "achternaam": "Visser",
   "nationaliteit": "Belgische",
   "leeftijd": 42,
   "gewicht": 69
},
{
   "voornaam": "Klaas",
   "achternaam": "Wever",
   "nationaliteit": "Nederlandse",
   "leeftijd": 73,
   "gewicht": 85
},
{
   "voornaam": "Bjorn",
   "achternaam": "Hakke",
   "nationaliteit": "Zweeds",
   "leeftijd": 18,
   "gewicht": 71
},
{
   "voornaam": "Jouke",
   "achternaam": "Dijkstra",
   "nationaliteit": "Fries",
   "leeftijd": 29,
   "gewicht": 82
},
{
   "voornaam": "Bo",
   "achternaam": "Wáng",
   "nationaliteit": "Chinees",
   "leeftijd": 38,
   "gewicht": 65
}];
//The age filter
var ageFilter = 0;

//The list of user divs
var divs = [];

//getting the body element
var body = document.getElementById('body');
body.style.width = "20em"; 

//The input field and button
var p = document.createElement('p');
p.innerHTML = "Leeftijdsfilter";
p.style.width = "20em";
var form = document.createElement('div');
form.style.display = "flex";
form.style.flexWrap = "wrap";

var input = document.createElement('input');

var button = document.createElement('button');
button.innerHTML = "submit"
button.onclick = x => {
   ageFilter = input.value
   show_users();
};
form.appendChild(p)
form.appendChild(input);
form.appendChild(button);
body.appendChild(form);

show_users()

function show_users(){
   //Deletes any existing divs
   divs.forEach(div => div.remove());
   //Loop trough the user 
   data.forEach(user => {
      var div = document.createElement('div');

      //If the user is older than the age filter
      if(user.leeftijd > ageFilter){
         //Loop trough the user properties
         for (const [key, value] of Object.entries(user)) {
            //Writes the user properties to a paragraph and adds it to a div
            var p = document.createElement('p');
            p.innerHTML = `${key}: ${value}`
            div.appendChild(p);
         }
         //Styles the div
         div.style.backgroundColor = "grey";
         //Adds the div to the body
         body.appendChild(div);
         divs.push(div);
      }
   });
   body.style.display = "flex";
   body.style.flexDirection = "column";
   body.style.rowGap = "1em";
}
