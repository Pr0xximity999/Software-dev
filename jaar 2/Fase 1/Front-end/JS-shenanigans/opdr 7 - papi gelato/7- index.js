//Customer data
var customer = {
    'type': '',
    'iceType': '',
    'iceNum': 0,
    'container': '',
    'flavours': { 'strawberry': 0, 'chocolate': 0, 'vanilla': 0 },
    'toppingCost': 0,
}

//Start
what_customer()

//Ask what kind of customer the customer is
function what_customer() {
    var input = prompt('Wat voor klant bent u? \nA) Particulier \nB) Zakelijk \nVul a of b in').toLowerCase()
    switch (input) {
        case 'a':
            customer.iceType = 'bolletje'
            customer.type = 'particulier'
            how_much_ice()
        case 'b':
            customer.iceType = 'liter'
            customer.type = 'zakelijk'
            how_much_ice()
        default:
            sorryPrompt()
            what_customer()
    }
}

//Asks how much icecream the customer wants
function how_much_ice() {
    iceNum = prompt(`Hoeveel ${customer.iceType}s ijs wilt u`)
    if (!checkNum(iceNum)) {
        how_much_ice()
    }
    customer.iceNum = parseInt(iceNum)

    if (customer.type == 'zakelijk') {
        choose_flavour()
    }
    else if (customer.iceNum >= 1 && customer.iceNum <= 3) {
        choose_flavour()
    }
    else if (customer.iceNum > 3 && customer.iceNum <= 8) {
        alert(`Dan krijgt u een bakje met ${customer.iceNum} ${customer.iceType}s`)
        customer.container == 'bakje'
        choose_flavour()
    }
    else if (customer.iceNum > 8) {
        alert('Sorry, zulke grote bakken hebben wij niet')
        how_much_ice()
    }
    else {
        sorryPrompt()
        how_much_ice()
    }
}

//Asks or the flavour
function choose_flavour() {
    alert('U heeft keuze uit 3 smaken:\nA) Aardbei\nC) Chocolade\nV) Vanille\nKies a, c of v')
    var flavour = ''
    var totquantity = 0
    //Loops trough the number of ice and lets the user choose what flavour they want
    for (let i = 1; i < customer.iceNum + 1; i++) {
        //Asks question based on customer type
        if (customer.type == 'particulier') { var flavour = prompt(`Welke smaak wilt u voor bolletje #${i}?\nA) Aardbei\nC) Chocolade\nV) Vanille\nKies a, c of v`).toLowerCase() }
        else if (customer.type == 'zakelijk') {
            if (totquantity >= customer.iceNum) {
                console.log('done');
                break
            }
            var flavour = prompt(`Welke smaak wilt u voor liter #${totquantity + 1}?\nA) Aardbei\nC) Chocolade\nV) Vanille\nKies a, c of v`).toLowerCase()
        }
        console.log(flavour);
        //Dependend on the awnser chooses the flavour
        switch (flavour) {
            case 'a':
                flavour = 'strawberry'
                break
            case 'c':
                flavour = 'chocolate'
                break
            case 'v':
                flavour = 'vanilla'
                break
            default:
                sorryPrompt()
                i--
                continue
        }

        //Lets the user choose the number of liters if they are zakelijk
        var quantity = 0
        if (customer.type == 'zakelijk') {
            while (true) {
                quantity = prompt('Hoeveel liter wilt u met deze smaak?')
                if (!checkNum(quantity)) { continue }
                else { quantity = parseInt(quantity) }
                if (totquantity + quantity > customer.iceNum) {
                    prompt('Dat is meer dan dat je besteld heeft')
                }
                else {
                    totquantity += quantity
                    break
                }
            }
        }
        else if (customer.type == 'particulier') {
            quantity = 1
        }
        customer.flavours[flavour] += quantity
        console.log(customer.flavours);
    }
    if (customer.type == 'particulier' && customer.container == '') {
        cup_or_cone()
    }
    checkout()
}

//Lets the user choose what container it wants
function cup_or_cone() {
    var container = prompt('Bakje of hoorntje\nWilt u een bakje of hoorntje?\nB) bakje\nH) hoorntje').toLowerCase()

    switch (container) {
        case 'b':
            customer.container = 'bakje'
            break
        case 'h':
            customer.container = 'hoorntje'
            break
        default:
            sorryPrompt()
            cup_or_cone()

    }
    alert(`Hier is uw ${customer.container} met ${customer.iceNum} ${customer.iceType}s`)
    choose_topping()
}

//Lets the user choose a topping
function choose_topping() {
    var topping = prompt('Kies uw topping:\nG) geen\nSl) slagroom\nSp) Sprinkels\nC) caramel').toLowerCase()
    switch (topping) {
        case 'g':
            break;
        case 'sl':
            customer.toppingCost += 0.5
            break;
        case 'sp':
            customer.toppingCost += customer.iceNum * 0.3
            break;
        case 'c':
            if (customer.container == 'hoorntje') {
                customer.toppingCost += 0.6
            }
            if (customer.container == 'bakje') {
                customer.toppingCost += 0.9
            }
            break;

        default:
            sorryPrompt()
            choose_topping();
    }
    checkout()
}


//Generates the receipt
function checkout() {
    totalCost = 0
    if (customer.type == 'particulier') {
        var bolletjesP = document.createElement('p')
        bolletjesP.innerHTML = `Bolletjes:   ${customer.iceNum} x &#8364;0.95 = &#8364;${customer.iceNum * 0.95}`
        document.getElementById('body').appendChild(bolletjesP)
        totalCost += customer.iceNum * 0.95

        //Hoorntje cost
        if (customer.container == 'hoorntje') {
            var hoorntjeP = document.createElement('p')
            hoorntjeP.innerHTML = `Hoorntje:    1 x &#8364;1.25 = &#8364;${1 * 1.25}`
            document.getElementById('body').appendChild(hoorntjeP)
            totalCost += 1 * 1.25
        }

        //Bakje cost
        if (customer.container == 'bakje') {
            var bakjeP = document.createElement('p')
            bakjeP.innerHTML = `Bakje:       1 x &#8364;0.75 = &#8364;${1 * 0.75}`
            document.getElementById('body').appendChild(bakjeP)
            totalCost += 1 * 0.75
        }

        //Topping cost
        if (customer.toppingCost > 0) {
            var toppingP = document.createElement('p')
            toppingP.innerHTML = `Topping:     1 x &#8364;${customer.toppingCost}  = &#8364;${customer.toppingCost}`
            document.getElementById('body').appendChild(toppingP)
            totalCost += customer.toppingCost
        }
        document.getElementById('body').appendChild(document.createElement('p'))//Whitespace

        plusP = document.createElement('p')
        plusP.innerHTML = '                         --------- +'
        document.getElementById('body').appendChild(plusP)

        totalCostP = document.createElement('p')
        totalCostP.innerHTML = `Totaal:                     &#8364;${totalCost}`
        document.getElementById('body').appendChild(totalCostP)
    }
    else if (customer.type == 'zakelijk') {
        literP = document.createElement('p')
        plusP = document.createElement('p')
        totalP = document.createElement('p')
        btwP = document.createElement('p')

        literP.innerHTML = `Liter:         ${customer.iceNum} x &#8364;9.80   = &#8364;${customer.iceNum * 9.80}`
        plusP.innerHTML = '                         --------- +'
        totalP.innerHTML = `Totaal:                 &#8364;${customer.iceNum * 9.80}`
        btwP.innerHTML = `BTW(9%):                &#8364;${customer.iceNum * 9.80 * 0.09}`

        document.getElementById('body').appendChild(literP)
        document.getElementById('body').appendChild(plusP)
        document.getElementById('body').appendChild(totalP)
        document.getElementById('body').appendChild(btwP)
    }

    goodbyeP = document.createElement('p')
    goodbyeP.innerHTML = 'Bedankt en tot ziens!'
    throw Error('Program done')
}

//Checking if the given number is whole
function checkNum(num) {
    try {
        var num = parseInt(num)
        if (num < 0) { throw Error }
        if (num == NaN) { throw Error }
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