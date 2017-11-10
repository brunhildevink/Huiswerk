def gemiddelde():
    zin = input('voer je zin in: ')
    woorden = len(zin.split())
    gemiddelde = len(zin) / woorden
    return gemiddelde

zin = ""
woorden = ""

print(gemiddelde())

