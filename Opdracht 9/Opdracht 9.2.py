import datetime
import csv

infile = open('inloggers.csv', 'a')


#gebruik hier een herhalingslus:
def writeFile():
    naam = input("Wat is je achternaam? ")
    voor1 = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")
    day = datetime.datetime.now().time()
    writeFunction = '{:10};{:10};{:3};{:10};{:20}\n'.format(day, naam, voor1, gbdatum, email)
    infile.write('{:10};{:10};{:3};{:10};{:20}\n'.format('datum', 'naam', 'voornaam', 'gbdatum', 'email'))
    infile.write(writeFunction)
    infile.close()
writeFile()
