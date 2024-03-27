midDayTemp = [15, 25, 28, 28, 29, 28, 23]
midNightTemp = [13, 14, 16, 18, 16, 12, 12]

def calAverageTemp(tempArr):
    total = 0
    for i in range(len(tempArr)):
        total += tempArr[i]
    return total / len(tempArr)

midDayAver = calAverageTemp(midDayTemp)
midNightAver = calAverageTemp(midNightTemp)

print("The average temperature for midday: ", round(midDayAver, 1))
print("The average temperature for midnight: ", round(midNightAver, 1))