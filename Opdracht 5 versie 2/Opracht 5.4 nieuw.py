import datetime

vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y")
n = []

def hardlopers(n):

    for i in hardlopersNamen:
        print("{:20}   {:10}".format(s, hardlopers(n)))

hardlopersNamen = [

hardlopers(n)


