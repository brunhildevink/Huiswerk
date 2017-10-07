maand = 2

def seizoen():

    if maand in range(3, 6):
        print('Lente')
    elif maand in range(6, 9):
        print('Zomer')
    elif maand in range(9, 11):
        print('Herfst')
    elif maand in range(11, 13) or range(1, 3):
        print('Winter')
    else:
        print('Ongeldig')
    return maand

seizoen()

