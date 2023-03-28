isKaasGeel = input("Is de kaas geel? ")
if isKaasGeel == "ja" :
    heeftKaasGaten = input("Heeft de kaas gaten? ")
    if heeftKaasGaten == "ja":
        isKaasDuur = input("Is de kaas belachelijk duur? ")
        if isKaasDuur == "ja":
            print("De kaas is emmenthaler")
        else:
            print("De kaas is leerdammer")
    else:
        isKaasHard = input("Is de kaas hard? ")
        if isKaasHard == "ja":
            print("De kaas is pammigaro reggiano")
        else:
            print("De kaas is goudse kaas")
else:
    isKaasBeschimmeld = input("Heeft de kaas blauwe schimmels? ")
    if isKaasBeschimmeld == "ja":
        heeftKaasKorst = input("Heeft de kaas een korst? ")
        if heeftKaasKorst == "ja":
            print("De kaas is bleu de rochbaron")
        else:
            print("De kaas is foume d'ambert ")
    else:
        heeftKaasKorst = input("Heeft de kaas een korst? ")
        if heeftKaasKorst == "ja":
            print("De kaas is camambert")
        else:
            print("De kaas is mozzeralla")