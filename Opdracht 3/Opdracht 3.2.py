leeftijd = int(input('Wat is je leeftijd?'))
paspoort = str(input('Ben je in het bezit van een geldig Nederlands paspoort? '))

if (leeftijd >= 18 and paspoort == 'ja'):
    print('Gefeliciteerd, je mag stemmen!')

else:
    print('Helaas, je mag niet stemmen.')