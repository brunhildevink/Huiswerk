import csv

with open("artikelen.csv", "r") as file:
    reader = csv.DictReader(file, delimiter=";")
    score = 0
    high = 0
    totaal = 0
    for i in reader:
        if eval(i["Prijs"]) > score:
            score = eval(i["Prijs"])
            high = i
        totaal += eval(i["Voorraad"])
    print("Het duurste artikel is {} en die kost {} Euro".format(high["Naam"],high["Prijs"]))
    print("Er zijn slechts {} exemplaren in voorraad van het product met nummer {}".format(high["Voorraad"],high["Artikelnummer"]))
    print("Totaal hebben wij {} producten in ons magazijn liggen".format(totaal))