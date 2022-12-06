#!/usr/bin/env python3

reference = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}

outcomeTables = {
    "Rock": {
        "Rock": "Draw",
        "Paper": "Lose",
        "Scissors": "Win",
    },
    "Paper": {
        "Rock": "Win",
        "Paper": "Draw",
        "Scissors": "Lose",
    },
    "Scissors": {
        "Rock": "Lose",
        "Paper": "Win",
        "Scissors": "Draw",
    },
}

choiceScores = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
}

outcomeScores = {
    "Lose": 0,
    "Draw": 3,
    "Win": 6,
}

with open(input("Input: "),mode='r') as adventInput:
    totalScore = 0
    for i in adventInput:
        decryptedRound = [reference[i[2]], reference[i[0]]]
        outcome = outcomeTables[decryptedRound[0]][decryptedRound[1]]
        totalScore += choiceScores[decryptedRound[0]] + outcomeScores[outcome]
    print(totalScore)
