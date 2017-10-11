day = {'Thu', 'Thu', 'Thu', 'Thu', 'Thu'}
dayNum = {'10', '10', '10', '10', '10'}
month = {'Mar', 'Mar', 'Mar', 'Mar', 'Mar'}
year = {'2016', '2016', '2016', '2016', '2016'}
time = {'10:45:52', '10:46:04', '10:47:27', '10:48:33', '10:48:42'}
name = {'Miranda', 'Piet', 'Sasha', 'Karel', 'Kemal'}

infile = open('hardlopers.txt', 'w')


print("{:3} {:2} {:3} {:4},   {:8}, {:10}".format(day,dayNum,month,year,time,name))