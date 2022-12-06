#!/usr/bin/env python3
totalPriorities = 0

def priorityConvert(letter):
    number = ord(letter)
    if number < 97:
        return number - 38
    else:
        return number - 96

with open(input(),mode='r') as adventInput:
    elfGroups = []
    for i in adventInput:
        if len(elfGroups) == 2:
            elfGroups.append(i[:len(i) - 1])
            badge = list(set(set(elfGroups[0]) & set(elfGroups[1])) & set(elfGroups[2]))[0]
            totalPriorities += priorityConvert(badge)
            elfGroups = []
        else:
            elfGroups.append(i[:len(i) - 1])

print(totalPriorities)
