if __name__ == '__main__':
    inputFile = open("input.txt", "r")

    score = 0
    for line in inputFile:
        opponentAction = line[0]
        myAction = line[2]

        if myAction == 'X':
            score += 1
        elif myAction == 'Y':
            score += 2
        elif myAction == 'Z':
            score += 3

        if opponentAction == 'A':
            if myAction == 'X':
                score += 3
            elif myAction == 'Y':
                score += 6
            elif myAction == 'Z':
                score += 0
        elif opponentAction == 'B':
            if myAction == 'X':
                score += 0
            elif myAction == 'Y':
                score += 3
            elif myAction == 'Z':
                score += 6
        if opponentAction == 'C':
            if myAction == 'X':
                score += 6
            elif myAction == 'Y':
                score += 0
            elif myAction == 'Z':
                score += 3

    print("Score: " + str(score))


    inputFile.close()