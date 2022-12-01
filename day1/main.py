def findMinIdx(arr):
    minIdx = 0
    minimum = arr[0]
    for j in range(len(arr)):
        if arr[j] < minimum:
            minimum = arr[j]
            minIdx = j
    return minIdx


if __name__ == '__main__':
    inputFile = open("input.txt", "r")

    curElfNr = 1
    curElfCals = 0
    topElvesNrs = [0, 0, 0]
    topElvesCals = [0, 0, 0]
    topMinIdx = 0

    for line in inputFile:
        if line == "\n":
            if curElfCals > topElvesCals[topMinIdx]:
                topElvesCals[topMinIdx] = curElfCals
                topElvesNrs[topMinIdx] = curElfNr
                topMinIdx = findMinIdx(topElvesCals)
            curElfNr += 1
            curElfCals = 0
        else:
            curElfCals += int(line)

    print("The top " + str(len(topElvesNrs)) + " elves are:")
    total = 0
    for i in range(len(topElvesNrs)):
        print(str(topElvesNrs[i]) + ": " + str(topElvesCals[i]))
        total += topElvesCals[i]
    print("They are carrying a total of " + str(total) + " calories.")

    inputFile.close()
