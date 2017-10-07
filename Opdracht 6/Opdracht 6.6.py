def menu():
    menu1 = '1: Ik wil weten hoeveel kluizen nog vrij zijn.'
    menu2 = '2: Ik wil een nieuwe kluis.'
    menu3 = '3: Ik wil even iets uit mijn kluis halen.'
    menu4 = '4: Ik geef mijn kluis terug.'

    print(menu1)
    print(menu2)
    print(menu3)
    print(menu4)

    try:
        a = int(input('Kies een optie uit het menu: '))
        if a == 1:
            print('Je hebt gekozen voor optie 1')
            infile = open('kluizen.txt', 'r')
            content = (str(infile.readlines())).split(',')
            print('Er zijn {} van de 12 kluizen over.'.format(12 - len(content)))
        elif a == 2:
            print('Je hebt gekozen voor optie 2')
        elif a == 3:
            print('Je hebt gekozen voor optie 3')
        elif a == 4:
            print('Je hebt gekozen voor optie 4')

    except:
        print('Voer een geldig nummer in.')

menu()

def menu2():
    infile = open('kluizen.txt', 'r')
    content = (str(infile.readlines())).split(', ')

    if len(content) == 12:
        print('Er zijn helaas geen kluisjes meer beschikbaar.')

    infile = open('kluizen.txt', 'r')
    content = infile.readlines()

menu2()