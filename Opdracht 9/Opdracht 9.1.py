def kosten_pp():
    while True:
        try:
            personen = int(input('Met hoeveel personen?'))
            while personen < 0:
                print('Oeps! Een negatief getal is niet geldig, probeer het nog eens.')
                personen = int(input('Met hoeveel personen?'))
            return personen

        except ValueError:
            print('Oeps! Dat is geen geldig nummer, probeer het nog eens.')

        except ZeroDivisionError:
            print('Oeps! Je kan niet door 0 delen, probeer het nog eens.')

        except:
            print('Oeps! Ongeldige invoer, probeer het nog eens.')


kosten = 4356
personen = kosten_pp()
print('De kosten bedragen {} euro per persoon.'.format((kosten / personen)))




