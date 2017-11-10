import time
import os.path

timeNow = time.strftime("%A %d %b %y at %H:%M, ")

def nieuweLoper(naam):

    if os.path.exists("hardlopers.txt") == True:
        data = open("hardlopers.txt", "a")
        data.writelines("{}{}\n".format(timeNow, naam))
        data.close()
    else:
        data = open("hardlopers.txt", "w")
        data.writelines("{}{}\n".format(timeNow, naam))
        data.close()

naam = input("Wat is de naam van de loper: ")
nieuweLoper(naam)