studenten = {'henk':9, 'Piet':6, 'Kaas':3, 'Jan':8, 'Joris':6, 'Klaas':9, 'Borax':10, 'Triggered':9, 'Nicememe': 10}

for a in studenten.keys():
    if studenten[a] >= 9:
        print(a, studenten[a], end=', ')