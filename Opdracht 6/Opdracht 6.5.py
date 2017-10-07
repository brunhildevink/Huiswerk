def nested():
    for j in range(1,11):
        for i in range(1,11):
            print(i,'x',j,'=','{}'.format(i * j, end=' '))
        print()
nested()