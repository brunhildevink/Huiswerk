def inlezen_beginstation():
    while True:
        beginstation = input("Wat is je beginstation: ")
        if beginstation in stations:
            return beginstation
        else:
            continue


def inlezen_eindstation():
    while True:
        eindstation = input("Wat is je eindstation: ")

        if eindstation in stations and int(stations.index(beginstation)) < int(stations.index(eindstation)):
            return eindstation
        else:
            print("Deze reis is niet mogelijk")
            continue


def omroepen_reis():
    print('Je reist van station {} naar station {}.'.format(beginstation, eindstation))
    print('Het beginstation {} is het {}e station in het traject.'.format(beginstation, int(stations.index(beginstation)+1)))
    print('Het eindstation {} is het {}e station in het traject.'.format(eindstation, int(stations.index(eindstation)+1)))
    print('De afstand bedraagt {} stations.'.format((int(stations.index(eindstation))) - int(stations.index(beginstation))))
    print('De kosten van deze reis bedragen {} euro.'.format(((int(stations.index(eindstation))) - int(stations.index(beginstation))) * 5))

stations = ['Schagen', 'Heerhugowaard','Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal',
            'Amsterdam Amstel', 'Utrecht Centraal', "'s-Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation()
eindstation = inlezen_eindstation()
omroepen_reis()

#omroepen_reis(stations, beginstation, eindstation)
