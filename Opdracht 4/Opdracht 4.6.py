def wijzig(letterlijst):

    print(letterlijst)

    letterlijst.pop()
    letterlijst.pop()
    letterlijst.pop()
    letterlijst.append("d")
    letterlijst.append("e")
    letterlijst.append("f")

    print(letterlijst)

letterlijst = ['a', 'b', 'c']
wijzig(letterlijst)