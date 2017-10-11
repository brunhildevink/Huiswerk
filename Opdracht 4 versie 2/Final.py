def standaardprijs(afstandKM):

    prijsKM = 0.80

    if afstandKM < 50:
        prijsTotaal = afstandKM * prijsKM
        return prijsTotaal

    elif afstandKM > 0.50:
        prijsTotaal = 15.0 + (afstandKM * 0.60)
        return prijsTotaal

def ritprijs(leeftijd, weekendrit, afstandKM):

    if weekendrit == 'zaterdag' or weekendrit == 'zondag':
        if leeftijd < 12 or leeftijd >= 65:
            standaardprijs(afstandKM) * 0.65
            return standaardprijs(afstandKM) * 0.65
        return standaardprijs(afstandKM)

    else:
        if leeftijd < 12 or leeftijd >= 65:
            return standaardprijs(afstandKM) * 0.7
        return standaardprijs(afstandKM)

weekendrit = 0
afstandKM = 0
prijsTotaal = ritprijs(65, 'zaterdag', 50)
print(prijsTotaal)