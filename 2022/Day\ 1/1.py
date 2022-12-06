#!/usr/bin/env python3
highestCalorie = [0, 0]
elf = 1
calorieCount = 0
calorieString = ""

adventInput = open(input(),mode='r').read()
for i in range(0, len(adventInput)):
    if adventInput[i] == "\n":
        if (i + 1) == len(adventInput) or adventInput[i + 1] == "\n":
            calorieCount += int(calorieString)
            if calorieCount > highestCalorie[1]:
                highestCalorie[0] = elf
                highestCalorie[1] = calorieCount
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

print(highestCalorie)
