try{
    var numOfPpl = parseInt(prompt("Hoeveel mensen wil je opgeven? (minimaal 3)"));
    if(isNaN(numOfPpl)){throw console.error();}
    if(numOfPpl < 3){throw console.error();}
}
catch{
    alert('you fool.\nyou absolute buffoon.\nyou think you can challenge me in my own realm?\nyou think you can rebel against my authority?\nyou dare come into my house and upturn my dining chairs and spill coffee grounds in my Keurig?\nyou thought you were safe in your chain mail armor behind that screen of yours.\nI will take these laminate wood floor boards and destroy you.\nI didn`t want war\nbut i didn`t start it\nYou absolute fucking idiot\nyou come into MY house\nyou suck MY dick\nand call ME GAY?!?\nbababooey')
    numOfPpl = 0
    location.reload()
}
var nameList = []
for (let i = 0; i < numOfPpl; i++) {
    var name = prompt("Voer een naam in")
    nameList.push(name);
}
document.getElementById('namen').innerHTML = `De namen zijn ${nameList}`;
document.getElementById('namen rev').innerHTML = `De namen in reverse zijn ${nameList.reverse()}`;