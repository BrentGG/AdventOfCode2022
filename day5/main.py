def fillStacks(stacks, lines):
    firstLine = True
    for i in range(len(lines) - 1, -1, -1):
        stackIdx = 0
        lineIdx = 1
        while True:
            if lines[i][lineIdx] != ' ':
                if firstLine:
                    stacks.append([lines[i][lineIdx]])
                else:
                    stacks[stackIdx].append(lines[i][lineIdx])
            if lines[i][lineIdx + 2] == '\n':
                firstLine = False
                break
            stackIdx += 1
            lineIdx += 4


if __name__ == '__main__':
    inputFile = open("input.txt", "r")

    stacks = []
    fillingStacks = True  # it's not necessary to automate the filling of stacks but it seems fun
    stackLines = []
    for line in inputFile:
        if fillingStacks:
            if line[1] == '1':
                fillingStacks = False
                fillStacks(stacks, stackLines)
            else:
                stackLines.append(line)
            continue
        if line == "\n":
            continue
        startFrom = line.find("from")
        startTo = line.find("to")
        amount = int(line[5:startFrom - 1])
        frm = int(line[startFrom + 5: startTo - 1]) - 1
        to = int(line[startTo + 3:]) - 1
        toAdd = stacks[frm][len(stacks[frm]) - amount:]
        toAdd.reverse()
        stacks[to].extend(toAdd)
        stacks[frm] = stacks[frm][:len(stacks[frm]) - amount]
    for stack in stacks:
        print(stack[len(stack) - 1], end="")
    print()

    inputFile.close()
