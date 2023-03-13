//Define the elements
var body = document.getElementsByClassName('bgc').item(0);
var div = document.getElementById('container');
var btnL = document.createElement('button');
var btnM = document.createElement('button');
var btnR = document.createElement('button');
var btns = [btnL, btnM, btnR]

//Body style
body.style.backgroundColor = "grey";

//Div style
div.style.backgroundColor = "white";
div.style.margin = "0 auto";
div.style.padding = "1em";
div.style.width = "30%";
div.style.display = "flex";
div.style.flexDirection = "row";
div.style.columnGap = "1em";
div.style.justifyContent = "space-between";

//Buttons style
btnL.innerHTML = "Button 1";
btnM.innerHTML = "Button 2";
btnR.innerHTML = "Button 3";

btnL.style.backgroundColor = "green";
btnM.style.backgroundColor = "red";
btnR.style.backgroundColor = "blue";

btns.forEach(btn => {
    btn.style.border = "none";
    btn.style.color = "white";
    btn.style.width = "10em";
    btn.style.height = "6em";
});

//Adding the events to the buttons
btnL.onclick = x => body.style.backgroundColor = "green"
btnM.onclick = x => body.style.backgroundColor = "red"
btnR.onclick = x => body.style.backgroundColor = "blue"

//Append the buttons to the div
div.appendChild(btnL)
div.appendChild(btnM)
div.appendChild(btnR)
