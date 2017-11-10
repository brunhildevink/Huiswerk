import random

def randomSom():
    sum1 = random.randrange(1,7)
    sum2 = random.randrange(1,7)
    sum3 = sum1 + sum2

    if sum1 == sum2:
        print('{} + {} = {:2}   (dubbel)'.format(sum1, sum2, sum3))
    if sum1 != sum2:
        print('{} + {} = {:2}'.format(sum1, sum2, sum3))

    return randomSom()

randomSom()