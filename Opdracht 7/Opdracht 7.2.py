def string():

    string = str(input('geef een string van 4 letters: '))

    while len(string) != 4:
        print('{} bevat {} letters.'.format(string, len(string)))
        string = str(input('geef een string van 4 letters: '))

    while len(string) == 4:
        print('Inlezen van correcte string: {} is geslaagd.'.format(string))
        break

string()