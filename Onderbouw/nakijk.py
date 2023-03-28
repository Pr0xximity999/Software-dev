import os
import os.path
from datetime import date
trello1 = ""
trello2 = ""
trello3 = ""
trello4 = ""
github1 = ""
github2 = ""
github3 = ""
github4 = ""
opdracht1 = ""
opdracht2 = ""
opdracht3 = ""
reuse1 = "yeet"
today = date.today()
if os.path.isfile("standard.txt"):
    f = open("standard.txt", "a")
else:
    f = open("standard.txt", "x")
    jij = input("\nwie ben je?")
    deNakijker = input("wie kijkt het na?")
    app = input("\ngebruik je de trello tijd extentie?\n klik enter als je dat gebruikt, vul iets in al gebruik je het niet")
    f.write(jij+";"+deNakijker+";"+app)
    
f.close()
save = input("\nwil je dit als een template opslaan, antwoord dan met een intager")
try:
    save2 = int(save) 
except:
    save2 = "yeet"
naam = input("\nnaam opdracht")
try:
    os.remove("nakijk-"+naam+".txt")
except:
    fd=1
try:
    file = open("nakijk-"+naam+".txt", "x")
except:
    try:
        os.remove("nakijk.txt")
    except:
        fd=1
    file = open("nakijk.txt", "x")
file.write("\n Naam van de opdracht: " + naam + "\n")
file.write("\n Datum: " + str(today.strftime("%d/%m/%Y")+"\n"))
f = open("standard.txt","r")
check = f.read().split(";")
file.write("\n Opdracht van: " + check[0] + "\n")
file.write("\n Nagekeken door: " + check[1] + "\n")
if save2 != "yeet":
    try:
        trello11 = check[3]
        trello21 = check[4]
        trello31 = check[5]
        trello41 = check[6]
        github11 = check[7]
        github21 = check[8]
        github31 = check[9]
        github41 = check[10]
        opdracht11 = check[11]
        opdracht21= check[12]
        opdracht31 = check[13]
        auto = 1
    except:
        auto = 0
    if auto == 1:
        reuse = input("\nwil je de zelfde antwoorden gebruiken als diegene die je hebt opgeslagen? antwoord dan met een intager")
        try:
            reuse1 = int(reuse) 
        except:
            reuse1 = "yeet"
f.close()
app = check[2]

if reuse1 == "yeet":
    file.write("\n\n\n\n\nPlanning\n")
    trello1 = input("\nzeg iets (dus geen directe enter) als je trello hebt gebruikt")
    if trello1 != "":
        trello1 = "True"
        file.write("\nIs er een planning gemaakt (op Trelle): ja\n")
        trello2 = input("\nzeg iets als de kaartjes op tijd ingesteld zijn")
        if trello2 != "":
            trello2 = "True"
            file.write("\nStaan er op de kaartjes uren ingeschat: ja\n")
        else:
            if app != "":
                file.write("\nStaan er op de kaartjes uren ingeschat: nee, maar dat kan niet op de app\n")
            else:
                file.write("\nStaan er op de kaartjes uren ingeschat: nee\n")
        trello3 = input("\nzeg iets als de planning goed is bijgehouden")
        if trello3 != "":
            trello3 = "True"
            file.write("\nIs de planning (goed) bijgehouden: ja\n")
        else:
            file.write("\nIs de planning (goed) bijgehouden: nee\n")
        trello4 = input("\nzeg iets als er bij inlevering een link naar je trello aanwezig is")
        if trello4 != "":
            trello4 = "True"
            file.write("\nIs er bij inleveren link naar planning aanwezig: ja\n")
        else:
            file.write("\nIs er bij inleveren link naar planning aanwezig: nee\n")
    else:
        file.write("\nIs er een planning gemaakt (op Trelle): nee\n")
        if app != "":
            file.write("\nStaan er op de kaartjes uren ingeschat: nee, maar dat kan niet op de app\n")
        else:
            file.write("\nStaan er op de kaartjes uren ingeschat: nee\n")
        file.write("\nIs de planning (goed) bijgehouden: nee\n")
        file.write("\nIs er bij inleveren link naar planning aanwezig: nee\n")

    file.write("\n\n\n\n\nGithub\n")
    github1 = input("\nzeg iets (dus geen directe enter) als je een REPO hebt gemaakt op github")
    if github1 != "":
        github1 = "True"
        file.write("\nIs er een REPO gemaakt voor de opdracht: ja\n")
        github2 = input("\nzeg iets als je meerdere commits hebt gebruikt")
        if github2 != "":
            github2 = "True"
            file.write("\nZijn er meerdere commints aanwezig: ja\n")
        else:
            file.write("\nZijn er meerdere commints aanwezig: nee\n")
        github3 = input("\nzeg iets als je commits goede beschrijvingen hebben")
        if github3 != "":
            github3 = "True"
            file.write("\nZijn er goede beschrijvingen aanwezig bij de commints: ja\n")
        else:
            file.write("\nZijn er goede beschrijvingen aanwezig bij de commints: nee\n")
        github4 = input("\nzeg iets als je bij het inleveren je een link naar je REPO hebt ingeleverd")
        if github4 != "":
            github4 = "True"
            file.write("\nIs er bij inleveren link naar REPO aanwezig: ja\n")
        else:
            file.write("\nIs er bij inleveren link naar REPO aanwezig: nee\n")
    else:
        file.write("\nIs er een REPO gemaakt voor de opdracht: nee\n")
        file.write("\nZijn er meerdere commints aanwezig: nee\n")
        file.write("\nZijn er goede beschrijvingen aanwezig bij de commints: nee\n")
        file.write("\nIs er bij inleveren link naar REPO aanwezig: nee\n")
    file.write("\n\n\n\n\nOpdracht\n") 
    opdracht1 = input("\nzeg iets als je voldoet aan de technische eisen")
    if opdracht1 != "":
        opdracht1 = "True"
        file.write("\nVoldoet de opdracht aan de gestelde technische eisen: ja\n")
    else:
        file.write("\nVoldoet de opdracht aan de gestelde technische eisen: nee\n")
    opdracht2 = input("\nzeg iets als je voldoet aan de gestelde functionele eisen")
    if opdracht2 != "":
        opdracht2 = "True"
        file.write("\nVoldoet de opdracht aan de gestelde functionele eisen: ja\n")
    else:
        file.write("\nVoldoet de opdracht aan de gestelde functionele eisen: nee\n")
    opdracht3 = input("\nzeg iets als je een ZIP hebt ingeleverd met alle opdrachten")
    if opdracht3 != "":
        opdracht3 = "True"
        file.write("\nIs er een ZIP file ingeleverd met alle opdrachten: ja\n")
    else:
        file.write("\nIs er een ZIP file ingeleverd met alle opdrachten: nee\n")
else:
    trello1 = check[3]
    trello2 = check[4]
    trello3 = check[5]
    trello4 = check[6]
    github1 = check[7]
    github2 = check[8]
    github3 = check[9]
    github4 = check[10]
    opdracht1 = check[11]
    opdracht2 = check[12]
    opdracht3 = check[13]
    file.write("\n\n\n\n\nPlanning\n")
    if trello1 != "":
        trello1 = "True"
        file.write("\nIs er een planning gemaakt (op Trelle): ja\n")
        if trello2 != "":
            trello2 = "True"
            file.write("\nStaan er op de kaartjes uren ingeschat: ja\n")
        else:
            if app != "":
                file.write("\nStaan er op de kaartjes uren ingeschat: nee, maar dat kan niet op de app\n")
            else:
                file.write("\nStaan er op de kaartjes uren ingeschat: nee\n")
        if trello3 != "":
            trello3 = "True"
            file.write("\nIs de planning (goed) bijgehouden: ja\n")
        else:
            file.write("\nIs de planning (goed) bijgehouden: nee\n")
        if trello4 != "":
            trello4 = "True"
            file.write("\nIs er bij inleveren link naar planning aanwezig: ja\n")
        else:
            file.write("\nIs er bij inleveren link naar planning aanwezig: nee\n")
    else:
        file.write("\nIs er een planning gemaakt (op Trelle): nee\n")
        if app != "":
            file.write("\nStaan er op de kaartjes uren ingeschat: nee, maar dat kan niet op de app\n")
        else:
            file.write("\nStaan er op de kaartjes uren ingeschat: nee\n")
        file.write("\nIs de planning (goed) bijgehouden: nee\n")
        file.write("\nIs er bij inleveren link naar planning aanwezig: nee\n")

    file.write("\n\n\n\n\nGithub\n")
    if github1 != "":
        github1 = "True"
        file.write("\nIs er een REPO gemaakt voor de opdracht: ja\n")
        if github2 != "":
            github2 = "True"
            file.write("\nZijn er meerdere commints aanwezig: ja\n")
        else:
            file.write("\nZijn er meerdere commints aanwezig: nee\n")
        if github3 != "":
            github3 = "True"
            file.write("\nZijn er goede beschrijvingen aanwezig bij de commints: ja\n")
        else:
            file.write("\nZijn er goede beschrijvingen aanwezig bij de commints: nee\n")
        if github4 != "":
            github4 = "True"
            file.write("\nIs er bij inleveren link naar REPO aanwezig: ja\n")
        else:
            file.write("\nIs er bij inleveren link naar REPO aanwezig: nee\n")
    else:
        file.write("\nIs er een REPO gemaakt voor de opdracht: nee\n")
        file.write("\nZijn er meerdere commints aanwezig: nee\n")
        file.write("\nZijn er goede beschrijvingen aanwezig bij de commints: nee\n")
        file.write("\nIs er bij inleveren link naar REPO aanwezig: nee\n")
    file.write("\n\n\n\n\nOpdracht\n") 
    if opdracht1 != "":
        opdracht1 = "True"
        file.write("\nVoldoet de opdracht aan de gestelde technische eisen: ja\n")
    else:
        file.write("\nVoldoet de opdracht aan de gestelde technische eisen: nee\n")
    if opdracht2 != "":
        opdracht2 = "True"
        file.write("\nVoldoet de opdracht aan de gestelde functionele eisen: ja\n")
    else:
        file.write("\nVoldoet de opdracht aan de gestelde functionele eisen: nee\n")
    if opdracht3 != "":
        opdracht3 = "True"
        file.write("\nIs er een ZIP file ingeleverd met alle opdrachten: ja\n")
    else:
        file.write("\nIs er een ZIP file ingeleverd met alle opdrachten: nee\n")
print("\nIndien de opdracht naar jouw mening niet voldaan is wat moet er dan nog aangepast worden om de opdracht succesvol af te ronden?")
rip = input("klik enter, om dit leeg te laten")
if rip != "":
    file.write("\n\n\n\n\nIndien de opdracht naar jouw mening niet voldaan is wat moet er dan nog aangepast worden om de opdracht succesvol af te ronden?\n\n")
    rip = input("\nnou vertel, wat is er mis (je hebt 3 input regels om het te typen)")
    file.write(rip+" \n")
    rip = input()
    file.write(rip+" \n")
    rip = input()
    file.write(rip+" \n")
else:
    file.write("\n\n\n\n\nIndien de opdracht naar jouw mening niet voldaan is wat moet er dan nog aangepast worden om de opdracht succesvol af te ronden?\n\n\n\n\n\n...\n\n")
top = input("klik enter om GEEN Tops te geven")
if top != "":
    file.write("\n\n\n\n\nWat zijn jouw TOPS:\n\n")
    top = input("\nnou vertel, wat zijn de tops (je hebt 3 input regels om het te typen)")
    file.write(top+"\n")
    top = input()
    file.write(top+" \n")
    top = input()
    file.write(top+" \n")
else:
    file.write("\n\n\n\n\nWat zijn jouw TOPS:\n\n\n\n\n\n...\n\n")
tip = input("klik enter om GEEN Tips te geven")
if tip != "":
    file.write("\n\n\n\n\nWat zijn jouw TIPS:\n\n")
    tip = input("\nnou vertel, wat zijn de tips (je hebt 3 input regels om het te typen)")
    file.write(tip+"\n")
    tip = input()
    file.write(tip+"\n")
    tip = input()
    file.write(tip+"\n")
else:
    file.write("\n\n\n\n\nWat zijn jouw TIPS:\n\n\n\n\n\n...\n\n")    
file.close()
if save2 != "yeet":
    f =open("standard.txt", "a+")
    f.truncate(0)
    f.seek(0)
    f.write(jij+";"+deNakijker+";"+app+";"+trello1+";"+trello2+";"+trello3+";"+trello4+";"+github1+";"+github2+";"+github3+";"+github4+";"+opdracht1+";"+opdracht2+";"+opdracht3)
    f.close()