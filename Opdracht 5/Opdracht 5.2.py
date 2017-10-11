def kaartnummers():

        infile = open('kaartnummers.txt', 'r')
        kaartnummer = infile.read(6)
        str(infile).split()
        persoon = (infile.read()[2:12])
        infile = open('kaartnummersOrganised.txt', 'w')
        infile.write(('{} heeft kaartnummer: {}'.format(persoon, kaartnummer)))
        infile.close()

kaartnummers()

