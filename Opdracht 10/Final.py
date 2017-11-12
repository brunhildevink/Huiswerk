import xmltools

# xmltools install lukt niet, error. zie pip_install_error.png
xml = xmltools.processXML("stations.xml")

stations_codes = []
synoniem = {}
lange_naam = []

for station in xml["Stations"]['Station']:
    stations_codes.append([i['Code'],station['Type']])
    if station['Synoniemen'] is not None:
        synoniem[station['Code']] = {}
        synoniem[station['Code']]['naam']=station["Namen"]['Lang']
        synoniem[station['Code']]['Syn']=[]

        for x in station["Synoniemen"]["Synoniem"]:
            synoniem[station['Code']]['Syn'].append(x)

    lange_naam.append([station["Code"],station["Namen"]["Lang"]])

print("Dit zijn de codes en types van de 4 stations:")
for station in stations_codes:
    print('{:4} - {}'.format(station[0],station[1]))

print("\nDit zijn alle stations met één of meer synoniemen:")
for station in synoniem:
    print("Code: {:3} - Volledige naam: {} - Synoniemen: {}".format(station,synoniem[station]["naam"],synoniem[station]["Syn"]))

print("\nDit is de lange naam van elk station:")
for station in lange_naam:
    print("{:4} - {}".format(station[0],station[1]))

