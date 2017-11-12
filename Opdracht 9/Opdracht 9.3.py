import csv

with open("gamers.csv", "r") as file:
    reader = csv.DictReader(file, delimiter=";")
    score = 0
    high = 0
    for naam in reader:
        if int(naam["punten"]) > score:
            score = int(naam["punten"])
            high = naam
    print("De hoogste score is: {} op {} behaald door {}".format(high["punten"],high["datum"],high["naam"]))