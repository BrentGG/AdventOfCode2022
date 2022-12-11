def inspect(item, operation, mod):
    if operation[6:] == "old":
        nr = item
    else:
        nr = int(operation[6:])
    if operation[4] == '*':
        item *= nr
    elif operation[4] == '+':
        item += nr
    if item >= mod:
        item = item % mod
    return item


if __name__ == '__main__':
    inputFile = open("input.txt", "r")

    monkeyItems = []
    monkeyOps = []
    monkeyTest = []
    monkeyThrow = []
    monkeyInspect = []
    mod = 1
    monkeyIdx = 0
    while True:
        inputFile.readline()
        monkeyInspect.append(0)
        # read items
        line = inputFile.readline()[18:]
        monkeyItems.append([])
        prevTempIdx = -1
        while True:
            tempIdx = line.find(" ", prevTempIdx + 1)
            if tempIdx < 0:
                break
            monkeyItems[monkeyIdx].append(int(line[prevTempIdx + 1:tempIdx - 1]))
            prevTempIdx = tempIdx
        monkeyItems[monkeyIdx].append(int(line[prevTempIdx + 1:]))
        # read operation
        line = inputFile.readline()
        monkeyOps.append(line[line.find("=") + 2:line.find("\n")])
        # read test
        line = inputFile.readline()
        monkeyTest.append(int(line[line.find("by") + 3:]))
        mod *= monkeyTest[monkeyIdx]
        # read throw
        monkeyThrow.append([])
        line = inputFile.readline()
        monkeyThrow[monkeyIdx].append(int(line[line.find("monkey") + 7:]))
        line = inputFile.readline()
        monkeyThrow[monkeyIdx].append(int(line[line.find("monkey") + 7:]))
        monkeyIdx += 1
        if inputFile.readline() == "":
            break

    roundNr = 1
    while roundNr <= 10000:
        # print(">>> ROUND " + str(roundNr))
        for monkeyIdx in range(len(monkeyItems)):
            # print("\tmonkey " + str(monkeyIdx) + ":")
            while len(monkeyItems[monkeyIdx]) > 0:
                monkeyInspect[monkeyIdx] += 1
                # print("\t\tmonkey inspects item with worry level " + str(monkeyItems[monkeyIdx][0]))
                monkeyItems[monkeyIdx][0] = inspect(monkeyItems[monkeyIdx][0], monkeyOps[monkeyIdx], mod)
                # print("\t\t\tworry level is now " + str(monkeyItems[monkeyIdx][0]))
                newMonkeyIdx = monkeyThrow[monkeyIdx][0] if monkeyItems[monkeyIdx][0] % monkeyTest[monkeyIdx] == 0 else monkeyThrow[monkeyIdx][1]
                # print("\t\t\titem thrown to monkey " + str(newMonkeyIdx))
                monkeyItems[newMonkeyIdx].append(monkeyItems[monkeyIdx][0])
                monkeyItems[monkeyIdx].pop(0)
        roundNr += 1
        # print()
    monkeyInspect.sort(reverse=True)
    print(monkeyInspect[0] * monkeyInspect[1])

    inputFile.close()
