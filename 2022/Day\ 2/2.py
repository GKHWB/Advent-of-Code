#!/usr/bin/env python3

reference = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win",
}

outcomeTables = {
    "Rock": {
        "Draw": "Rock",
        "Lose": "Scissors",
        "Win": "Paper",
    },
    "Paper": {
        "Win": "Scissors",
        "Draw": "Paper",
        "Lose": "Rock",
    },
    "Scissors": {
        "Lose": "Paper",
        "Win": "Rock",
        "Draw": "Scissors",
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
        choice = outcomeTables[decryptedRound[1]][decryptedRound[0]]
        totalScore += choiceScores[choice] + outcomeScores[decryptedRound[0]]
    print(totalScore)
