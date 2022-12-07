if __name__ == '__main__':
    inputFile = open("input.txt", "r")

    dirs = [0]
    parentIdxs = [-1]
    currentIdx = 0
    for line in inputFile:
        if line == "$ cd /\n":
            dirs[parentIdxs[currentIdx]] += dirs[currentIdx]
            currentIdx = 0
        elif line == "$ cd ..\n":
            # dirs[parentIdxs[currentIdx]] += dirs[currentIdx]
            currentIdx = parentIdxs[currentIdx]
        elif line[:4] == "$ cd":
            dirs.append(0)
            parentIdxs.append(currentIdx)
            currentIdx = len(dirs) - 1
        elif line == "$ ls\n":
            pass
        elif line[:3] != "dir":
            dirs[currentIdx] += int(line[:line.find(" ")])

    count = 0
    for i in range(len(dirs) - 1, -1, -1):
        for j in range(len(dirs)):
            if parentIdxs[j] == i:
                count += dirs[j]
        dirs[i] += count
        count = 0

    neededSpace = 30000000 - (70000000 - dirs[0])
    minimum = dirs[0]
    for d in dirs:
        if neededSpace <= d < minimum:
            minimum = d
    print(minimum)

    inputFile.close()
