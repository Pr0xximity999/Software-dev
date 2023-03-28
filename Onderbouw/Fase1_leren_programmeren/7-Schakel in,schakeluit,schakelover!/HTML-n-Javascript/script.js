var btn = document.createElement('button');
btn.style.margin = '10px';
btn.innerHTML = '...';
document.body.appendChild(btn);

// schijf hier tussen je code
const buttonStates = ["on", "off"];
const lightStates = ["yellow", "black"];
updateState();
btn.onclick = function() {updateState()};

function updateState(){
    buttonStates.reverse();
    lightStates.reverse();
    console.log('The screen is ' + buttonStates[0])
    btn.textContent = "Turn the light " + buttonStates[0];
    document.body.style.backgroundColor = lightStates[0];
}   
// schijf hier tussen je code