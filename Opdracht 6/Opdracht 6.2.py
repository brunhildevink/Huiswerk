def boodschappen():

    lijst = input('Geef een lijst met minimaal 10 items: ')
    lijstSplitted = lijst.split(' ')

    if len(lijstSplitted) >= 10:
        for a in lijstSplitted:
            if len(a) == 4:
                print(a)

    else:
        print('Het moet minimaal 10 items bevatten!')

boodschappen()