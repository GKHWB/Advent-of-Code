#!/usr/bin/env python3
highestCalories = [[0, 0], [0, 0], [0, 0]]
elf = 1
calorieCount = 0
calorieString = ""

def swap(givenList, firstIndex, secondIndex):
    firstHolder = givenList[firstIndex]
    secondHolder = givenList[secondIndex]
    givenList[firstIndex] = secondHolder
    givenList[secondIndex] = firstHolder
    return givenList

def orderedInsert(givenList):
    givenList.append([elf, calorieCount])
    for i in reversed(range(0, len(givenList))):
        if i == (len(givenList)-1):
            continue
        if givenList[i][1] < givenList[i+1][1]:
            givenList = swap(givenList, i, i+1)
    givenList.pop()
    return givenList



adventInput = open(input(),mode='r').read()
for i in range(0, len(adventInput)):
    if adventInput[i] == "\n":
        if (i + 1) == len(adventInput) or adventInput[i + 1] == "\n":
            calorieCount += int(calorieString)
            highestCalories = orderedInsert(highestCalories)
            calorieCount = 0
            calorieString = ""
            elf += 1
        else:
            try:
                calorieCount += int(calorieString)
                calorieString = ""
            except:
                continue
    else:
        calorieString += str(adventInput[i])

finalSum = (highestCalories[0][1] + highestCalories[1][1] + highestCalories[2][1])
print(finalSum)
