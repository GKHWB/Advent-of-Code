#!/usr/bin/env python3
fullyContained = 0

with open(input("Input: "),mode='r') as adventInput:
    for i in adventInput:
        ranges = ["", "", "", ""]
        counter = 0
        for j in i.strip():
            if j == '-' or j == ',':
                counter += 1
            else:
                ranges[counter] += j
        for j in range(0, len(ranges)):
            ranges[j] = int(ranges[j])
        rangeOne = range(ranges[0], ranges[1]+1)
        rangeTwo = range(ranges[2], ranges[3]+1)
        if set(rangeOne) & set(rangeTwo) != set():
            fullyContained += 1
print(fullyContained)
