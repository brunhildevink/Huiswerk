infile = open('kaartnummers.txt')

for naam in infile.readlines():
    temp = naam.split(sep=',')
    print(temp[1].strip('\n ') + " heeft kaartnummer: " + temp[0])

infile.close()