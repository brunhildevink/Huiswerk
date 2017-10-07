nummers = "5-9-7-1-7-8-3-2-4-8-7-9"

def list():
    mylist = nummers.split('-')
    return mylist
list()

gesorteerd = sorted(list())
kleinste = map(int, list())
grootste = map(int, list())

def gemiddelde():
    sumGetallen = sum(map(int, list()))
    lengte = len(list())
    som = sumGetallen / lengte
    return som

sumGetallen = sum(map(int, list()))

print('De gesorteerde lijst is:             {}'.format(gesorteerd))
print('Het kleinste getal is:               {}'.format(min(kleinste)))
print('Het grootste getal is:               {}'.format(max(grootste)))
print('De lengte van de lijst is:           {}'.format(len(list())))
print('De som van de lijst is:              {}'.format(sumGetallen))
print('Het gemiddelde van de lijst is:      {}'.format(gemiddelde()))
