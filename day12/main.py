import time


def isPossibleMove(heightMap, moveTo, moveFrom, covered):
    if moveTo[0] < 0 or moveTo[0] >= len(heightMap) or moveTo[1] < 0 or moveTo[1] >= len(heightMap[0]):
        return False
    if moveTo in covered:
        return False
    if heightMap[moveTo[0]][moveTo[1]] > heightMap[moveFrom[0]][moveFrom[1]] + 1:
        return False
    return True


def pathFind(heightMap, end, pos, steps, covered):
    covered.append(pos)
    if pos == end:
        return steps
    else:
        values = []
        if isPossibleMove(heightMap, [pos[0] - 1, pos[1]], pos, covered):  # move up
            values.append(pathFind(heightMap, end, [pos[0] - 1, pos[1]], steps + 1, covered.copy()))
        if isPossibleMove(heightMap, [pos[0] + 1, pos[1]], pos, covered):  # move down
            values.append(pathFind(heightMap, end, [pos[0] + 1, pos[1]], steps + 1, covered.copy()))
        if isPossibleMove(heightMap, [pos[0], pos[1] - 1], pos, covered):  # move left
            values.append(pathFind(heightMap, end, [pos[0], pos[1] - 1], steps + 1, covered.copy()))
        if isPossibleMove(heightMap, [pos[0], pos[1] + 1], pos, covered):  # move right
            values.append(pathFind(heightMap, end, [pos[0], pos[1] + 1], steps + 1, covered.copy()))
        if -1 in values:
            values.remove(-1)
        if len(values) == 0:
            return -1
        else:
            values.sort()
            return values[0]


if __name__ == '__main__':
    inputFile = open("input.txt", "r")

    heightMap = []
    start = [0, 0]
    end = [0, 0]
    row = 0
    for line in inputFile:
        heightMap.append([])
        col = 0
        for c in line:
            if c == 'S':
                start = [row, col]
                heightMap[row].append(0)
            elif c == 'E':
                end = [row, col]
                heightMap[row].append(25)
            elif c != '\n':
                heightMap[row].append(ord(c) - 97)
            col += 1
        row += 1

    startTime = time.time()
    print(pathFind(heightMap, end, start, 0, []))
    print("Execution took " + str(time.time() - startTime) + " seconds.")

    inputFile.close()
