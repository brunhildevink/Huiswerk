infile = open('kaartnummers.txt')
content = infile.readlines()
lines = len(content)

grootste = ""
kleinste = ""

#berekent grootste kaartnummer

def grootsteKaartnummer(grootste):
    grootste = max(content)
    return grootste[0:6]

#berekent kleinste kaartnummer

def kleinsteKaartnummer(kleinste):
    kleinste = min(content)
    return kleinste[0:6]

#zoekt regel van grootste nummer op

lookup = str(645345)
num = ""

def indexKaartnummer(num):
    with open('kaartnummers.txt') as myFile:
        for num, line in enumerate(myFile, 1):
            if lookup in line:
                return(num)

grootsteKaartnummer(grootste)
kleinsteKaartnummer(kleinste)
indexKaartnummer(num)

print('Deze file telt {} regels.'.format(lines))
print('Het grootste kaartnummer is: {} en deze staat op regel {}'.format(grootsteKaartnummer(grootste),(indexKaartnummer(num))))
print('Het kleinste kaartnummer is: {}.'.format(kleinsteKaartnummer(kleinste)))

infile.close()