studentencijfers = [[95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0]]

def gemiddelde_per_student(studentencijfers):
    a = sum(studentencijfers[0]) / len(studentencijfers[0])
    b = sum(studentencijfers[1]) / len(studentencijfers[1])
    c = sum(studentencijfers[2]) / len(studentencijfers[2])
    return a, b, c

def gemiddelde_van_alle_studenten(studentencijfers):
    som = sum(studentencijfers[0]) + sum(studentencijfers[1]) + sum(studentencijfers[2])
    lengte = len(studentencijfers[0]) + len(studentencijfers[1]) + len(studentencijfers[2])
    gemiddeldeStudenten = som / lengte
    return gemiddeldeStudenten

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))
