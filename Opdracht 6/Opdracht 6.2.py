#userList = eval(input("Geef lijst met minimaal 10 strings: "))
userList = ["boter", "kaas", "bier", "pizza", "thee", "drop", "koek", "cola", "boterham", "stamppot"]
newList = []

for i in userList:
    if len(i) == 4:
        newList.append(i)

print("De nieuw-gemaakte list met alle vier-letter strings is: {}" .format(newList))