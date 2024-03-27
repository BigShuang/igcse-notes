midDayTemp = [15, 25, 28, 28, 29, 28, 23]
midNightTemp = [13, 14, 16, 18, 16, 12, 12]

def getHighestDay(tempArr):
    highestIndex = 0
    for i in range(len(tempArr)):
        if tempArr[i] > tempArr[highestIndex]:
            highestIndex = i
    return lowestIndex

def getLowestDay(tempArr):
    lowestIndex = 0
    for i in range(len(tempArr)):
        if tempArr[i] < tempArr[lowestIndex]:
            lowestIndex = i
    return lowestIndex

midDayHighIndex = getHighestDay(midDayTemp)
midDayLowIndex = getLowestDay(midDayTemp)

print("The day with the highest midday temperature: ", midDayHighIndex, 
    " and its' temperature is", midDayTemp[midDayHighIndex])
print("The day with the lowest midday temperature: ", midDayHighIndex, 
    " and its' temperature is", midDayTemp[midDayLowIndex])