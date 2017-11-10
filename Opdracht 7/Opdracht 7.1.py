def som():

    lijst = []
    nummer = eval(input('geef een nummer'))
    lijst.append(nummer)

    while nummer != 0:
        nummer = eval(input('geef een nummer'))
        lijst.append(nummer)

    while nummer == 0 or nummer :
        print('Er zijn {} getallen ingevoerd. De som is: {}'.format((len(lijst) - 1), sum(lijst)))
        break

som()
