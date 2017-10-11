def convert(gradenC):

    gradenF = (gradenC * 1.8) + 32
    return gradenF

def table():
    print('  C        F')
    for temp in range(-30, 81, 10):
        print("{:4}     {:4}".format(temp, convert(temp)))


table()