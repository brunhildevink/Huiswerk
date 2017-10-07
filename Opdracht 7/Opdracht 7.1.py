def som():

    nummer = eval(input('geef een nummer'))

    while nummer >= 1:
        nummer = eval(input('geef een nummer'))

    while nummer == 0:
        listNummer = [nummer]
        print('Er zijn  ingevoerd. De som is: {}'.format(sum(listNummer)))
        list = str(nummer).split()
        break



def somOpgeteld(som):

    nummer = 0
    opgeteld = sum(int(nummer))


som()
#somOpgeteld(som)