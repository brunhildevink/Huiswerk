#5.1

def convert(gradenCelcius):

    conversionCelciusFahrenheit = (gradenCelcius * 1.8) + 32
    return conversionCelciusFahrenheit


def table():
    print('C        F')
    for celciusValues in range(-30, 41, 10):
        print('{:4}   {:4}'.format(celciusValues, convert(celciusValues)))



conversionCelciusFahrenheit = 1
table()