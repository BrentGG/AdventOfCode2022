if __name__ == '__main__':
    inputFile = open("input.txt", "r")

    score = 0
    for line in inputFile:
        opponentAction = line[0]
        goal = line[2]

        if opponentAction == 'A':
            if goal == 'X':  # choose scissors
                score += 3 + 0
            elif goal == 'Y':  # choose rock
                score += 1 + 3
            elif goal == 'Z':  # choose paper
                score += 2 + 6
        elif opponentAction == 'B':
            if goal == 'X':  # choose rock
                score += 1 + 0
            elif goal == 'Y':  # choose paper
                score += 2 + 3
            elif goal == 'Z':  # choose scissors
                score += 3 + 6
        if opponentAction == 'C':
            if goal == 'X':  # choose paper
                score += 2 + 0
            elif goal == 'Y':  # choose scissors
                score += 3 + 3
            elif goal == 'Z':  # choose rock
                score += 1 + 6

    print("Score: " + str(score))

    inputFile.close()
