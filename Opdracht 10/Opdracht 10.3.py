a = 3

def f(y):
    global a
    a = 9
    return 2*y + a

print(a)

#antwoord = B (3)





x = 1
y = 4

def fun():
    x = 2
    global y
    y = 3
    print(y, end = ' ')

fun()
print(y, end = ' ')

#antwoord = D (3 3)




x = 2
y = 5

def fun():
    y = 3
    global x
    x = 1
    print(x*y, end = ' ')
    return x*y

x = fun()
print(x*y, end = ' ')

#antwoord = A (3 15)



a = 3

def fun1():
    global a
    print("a:", a, end = ' ')
    b = 7
    a = 0
    return b

def fun2(y):
    a = y + fun1()
    b = 7
    a += 1
    return a

a = 9
fun2(5)
print("a:", a)

#antwoord = A (a: 9 a:13)




x = 1
y = 4

def doe1():
    global x
    y = 7
    x = 0
    return y

def doe2():
    x = doe1()
    x += 1
    return x

x = doe1()
print(x)

#antwoord = C (7)



a = 5

def fun1():
    global a
    b = 2
    a = 4
    return a+b

def fun2(y):
    global a
    a = y + fun1()
    a += 1
    return a
    print("a:", a, end = ' ')

a = fun2(3)
print("a:", a)

#antwoord = D (a: 5 a:10)


x = 1
y = 3

def doe1():
    global x
    y = 4
    x = 0
    return x+y

def doe2():
    x = doe1()
    x += 2
    return x

doe2()
print(x)

#antwoord = 0??? ik dacht 6


def doe1():
    y = 7
    x = 0
    return y

def doe2():
    global x
    x = doe1()
    x += 1

doe2()
print(x)

#antwoord = D (8)
