studenten = []

def namen_klas():

    namen = input('Voer naam in: ')
    studenten.append(namen)
    print(namen)

    while namen != '':
        namen = input('Voer naam in: ')
        studenten.append(namen)
        print(namen)

namen_klas()

def frequency(studenten):
    counters = {}

    for naam in studenten:
        if naam in counters:
            counters[naam] += 1
        else:
            if naam == '':
                break
            counters[naam] = 1

    for naam in counters:
        if counters[naam] > 1:
            print('Er zijn {} studenten met de naam {}'.format(counters[naam], naam))
        else:
            print('Er is {} student met de naam {}'.format(counters[naam], naam))

frequency(studenten)