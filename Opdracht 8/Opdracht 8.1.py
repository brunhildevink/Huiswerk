groen = {'weert', 'heeze', 'geldrop', 'eindhoven', 'beukenlaan', 'best', 'boxtel'}
rood = {'deurne', 'helmond brouwhuis', 'helmond', "helmond aan 't hout", 'eindhoven', 'beukenlaan', 'best', 'boxtel'}

print(groen & rood)
print(groen - rood)
stations = groen | rood
print(stations)