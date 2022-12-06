#!/usr/bin/env python3
totalPriorities = 0

def priorityConvert(letter):
    number = ord(letter)
    if number < 97:
        return number - 38
    else:
        return number - 96

with open(input(),mode='r') as adventInput:
    for i in adventInput:
        compartmentOne = i[0:int((len(i) - 3)/2)+ 1]
        compartmentTwo = i[int((len(i) - 3)/2)+ 1:len(i)]
        for j in list(set(compartmentOne) & set(compartmentTwo))[0]:
            totalPriorities += priorityConvert(j)

print(totalPriorities)
