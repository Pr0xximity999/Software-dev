//Declare variables
var buttons = 30;
var div = document.getElementById('container')
var btns = []

//Make the buttons
for (let i = 0; i < buttons; i++) {
    var btn = document.createElement('button');
    btn.style.border = "none";
    btn.style.backgroundColor = "green";
    btn.innerHTML = i + 1;
    btn.style.fontSize = "40px"
    btn.style.flex = "1 0 17%"
    btn.style.height = "3em";
    btns.push(btn)
    div.appendChild(btn)
}
btns.forEach(btn => btn.onclick = x =>{
    var colours = ['green', 'red', 'orange', 'yellow', 'white', 'blue', 'purple', 'pink', 'black']
    var colorNum = colours.indexOf(btn.style.backgroundColor)
    if(colorNum != colours.length){
        colorNum++
    }
    if(colorNum == colours.length){
        btn.remove()
    }
    console.log(colorNum);
    btn.style.backgroundColor = colours[colorNum]
})

//Div styling
div.style.backgroundColor = "grey";
div.style.margin = "0 auto";
div.style.padding = "1em";
div.style.width = "60%";
div.style.display = "flex";
div.style.flexDirection = "row";
div.style.flexWrap = "wrap";
div.style.justifyContent = "space-between"
div.style.columnGap = "1em";
div.style.rowGap = "1em";