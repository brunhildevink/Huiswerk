def kwadraten_som(grondgetallen):

    totaal = 0

    for a in grondgetallen:
        totaal += pow(a,a)

    return totaal

grondgetallen = [1, 3, 1, -14]
totaal = kwadraten_som(grondgetallen)

print(totaal)