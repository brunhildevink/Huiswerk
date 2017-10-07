nummers = "5-9-7-1-7-8-3-2-4-8-7-9"

def list():
    mylist = nummers.split('-')
    return mylist
list()

gesorteerd = (sorted(list()))
kleinste = map(int, list())
grootste = map(int, list())

def gemiddelde():
    sumGetallen = sum(map(int, list()))
    lengte = len(list())
    som = sumGetallen / lengte
    return som

print('de gesorteerde list is {}'.format(gesorteerd))
print('het kleinste getal is {}'.format(min(kleinste)))
print('het grootste getal is {}'.format(max(grootste)))
print('de lengte van de lijst is {}'.format(len(list())))
print('het gemiddelde van de lijst is {}'.format(gemiddelde()))
