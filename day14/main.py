if __name__ == '__main__':
    inputFile = open("input.txt", "r")

    xMin, xMax = 9999, 0
    yMin, yMax = 9999, 0
    for line in inputFile:
        while True:
            index = line.find("->")
            if index < 0:
                index = len(line)
            coordString = line[:index]
            index2 = coordString.find(",")
            x, y = int(coordString[:index2]), int(coordString[index2 + 1:])
            xMin = x if x < xMin else xMin
            xMax = x if x > xMax else xMax
            yMin = y if y < yMin else yMin
            yMax = y if y > yMax else yMax
            if line.find("->") < 0:
                break
            line = line[index + 3:]

    scan = []
    for i in range(yMax + 1):
        scan.append([])
        for j in range(xMax - xMin + 1):
            scan[i].append(0)
    scan[0][500 - xMin] = 2

    inputFile.close()
    inputFile = open("input.txt", "r")

    prevX, prevY = -1, -1
    for line in inputFile:
        while True:
            index = line.find("->")
            if index < 0:
                index = len(line)
            coordString = line[:index]
            index2 = coordString.find(",")
            x, y = int(coordString[:index2]) - xMin, int(coordString[index2 + 1:])
            if prevX != -1:
                if prevX == x:
                    for i in range(prevY if prevY < y else y, y + 1 if y > prevY else prevY + 1):
                        scan[i][x] = 1
                elif prevY == y:
                    for i in range(prevX if prevX < x else x, x + 1 if x > prevX else prevX + 1):
                        scan[y][i] = 1
            prevX, prevY = x, y
            if line.find("->") < 0:
                break
            line = line[index + 3:]
        scan[prevY][prevX] = 1
        prevX, prevY = -1, -1

    startX, startY = 500 - xMin, 0
    toRest = 0
    intoVoid = False
    while not intoVoid:
        x, y = startX, startY
        while True:
            if y + 1 >= len(scan):
                intoVoid = True
                break
            if scan[y + 1][x] == 0:
                y += 1
                continue
            if x - 1 < 0:
                intoVoid = True
                break
            if scan[y + 1][x - 1] == 0:
                x -= 1
                continue
            if x + 1 >= len(scan[0]):
                intoVoid = True
                break
            if scan[y + 1][x + 1] == 0:
                x += 1
                continue
            scan[y][x] = 3
            toRest += 1
            break

    for row in scan:
        for col in row:
            if col == 0:
                print(".", end="")
            elif col == 1:
                print("#", end="")
            elif col == 2:
                print("+", end="")
            elif col == 3:
                print("o", end="")
        print()
    print(toRest)

    inputFile.close()
