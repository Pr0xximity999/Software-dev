//Customer data
var customer = {
    'type': '',
    'iceType': '',
    'iceNum': 0,
    'container': '',
    'flavours': { 'strawberry': 0, 'chocolate': 0, 'vanilla': 0 }
}

//Start
whatCustomer()

//Ask what kind of customer the customer is
function whatCustomer() {
    var input = prompt('Wat voor klant bent u? \nA) Particulier \nB) Zakelijk \nVul a of b in').toLowerCase()
    switch (input) {
        case 'a':
            customer['iceType'] = 'bolletje'
            howMuchIce()
        case 'b':
            customer['iceType'] = 'liter'
            howMuchIce()
        default:
            sorryPrompt()
            whatCustomer()
            return
    }
}

//Asks how much icecream the customer wants
function howMuchIce() {
    iceNum = prompt(`Hoeveel ${customer['iceType']}s ijs wilt u`)
    if (!checkNum(iceNum)) {
        howMuchIce()
    }
    customer['iceNum'] = parseInt(iceNum)

    if (customer['type'] == 'zakelijk') {
        chooseFlavour()
    }
    else if (customer['iceNum'] >= 1 && customer['iceNum'] <= 3) {
        chooseFlavour()
    }
    else if (customer['iceNum'] > 3 && customer['iceNum'] < 8) {
        alert(`Dan krijgt u een bakje met ${customer['iceNum']}`)
        customer['container'] == 'bakje'
        chooseFlavour()
    }
    else if (customer['iceNum'] > 8) {
        alert('Sorry, zulke grote bakken hebben wij niet')
        howMuchIce()
    }
    else {
        sorryPrompt()
        howMuchIce()
    }
}

//Asks or the flavour
function chooseFlavour() {
    alert('U heeft keuze uit 3 smaken:\nA) Aardbei\nC) Chocolade\nV) Vanille\nKies a, c of v')
    console.log(customer['iceNum']);
    for (let i = 1; i < customer['iceNum'] + 1; i++) {
        if(customer['type'] == 'particulier'){}
        var flavour = prompt(`Welke smaak wilt u voor bolletje #${i}?\nA) Aardbei\nC) Chocolade\nV) Vanille\nKies a, c of v`).toLowerCase()
        switch (flavour) {
            case 'a':
                customer['flavours']['strawberry'] += 1
                break
            case 'c':
                customer['flavours']['chocolate'] += 1
                break
            case 'v':
                customer['flavours']['vanilla'] += 1
                break
            default:
                sorryPrompt()
                i--
                continue
        }
        console.log(customer['flavours']);
        console.log(i);
    }
}

//Checking if the given number is whole
function checkNum(num) {
    try {
        var num = parseInt(num)
        if (num < 0) { throw Error }
    }
    catch {
        sorryPrompt()
        return false
    }
    return true
}
//In case something invalid happens
function sorryPrompt() {
    alert('Dat is geen geldige optie')
}