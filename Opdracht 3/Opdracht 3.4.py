numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

for c in numbers:
    if c % 2 == 0:
        print(c)
    else:
        print('Het getal {} is oneven.'.format(c))