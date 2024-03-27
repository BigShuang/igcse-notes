MiddayTemperature = [0 for i in range(30)]
MidnightTemperature = [0 for i in range(30)]

for i in range(30):
    DayTemp = float(input("Enter midday temperature for day", i))
    NightTemp = float(input("Enter midnight temperature for day", i))
    
    MiddayTemperature[i] = DayTemp
    MidnightTemperature[i] = NightTemp
