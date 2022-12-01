if __name__ == '__main__':
    inputFile = open("input.txt", "r")

    curElfNr = 1
    curElfCals = 0
    maxElfNr = 0
    maxElfCals = 0
    for line in inputFile:
        if line == "\n":
            if curElfCals > maxElfCals:
                maxElfNr = curElfNr
                maxElfCals = curElfCals
            curElfNr += 1
            curElfCals = 0
        else:
            curElfCals += int(line)

    print("Elf number " + str(maxElfNr) + " is carrying the most calories (" + str(maxElfCals) + ")")

    inputFile.close()
