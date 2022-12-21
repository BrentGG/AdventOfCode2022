def findCoord(index, array):
    i = 1
    idx = array.index(0) + 1
    while i <= index:
        i += 1
        idx += 1
        if idx > len(array) - 1:
            idx = 0
    return array[idx - 1]


if __name__ == '__main__':
    inputFile = open("testinput.txt", "r")

    ogArray = []
    for line in inputFile:
        ogArray.append(int(line))

    ogArray[len(ogArray) - 1] = 8
    array = ogArray.copy()
    print(array)
    for number in ogArray:
        print(number, end=": ")
        idx = array.index(number)
        array.pop(idx)
        tempNumber = number
        newIdx = idx
        while tempNumber != 0:
            newIdx += 1 if tempNumber > 0 else -1
            if newIdx == 0:
                newIdx = len(array) - 1
            elif newIdx == len(array):
                newIdx = 0
            tempNumber -= 1 if tempNumber > 0 else -1
        if number > 0:
            array.insert(newIdx, number)
        else:
            array.insert(newIdx + 1, number)
        print(array)
    print(array)
    print((findCoord(1000, array) + findCoord(2000, array) + findCoord(3000, array)))

    inputFile.close()
