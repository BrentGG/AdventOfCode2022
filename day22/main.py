def rotate(facing, rotation):
    if rotation == 'R':
        return facing + 1 if facing + 1 <= 3 else 0
    if rotation == 'L':
        return facing - 1 if facing - 1 >= 0 else 3
    return facing


def getSection(row, col):
    if 0 <= row < 50:
        if 50 <= col < 100:
            return 1
        elif 100 <= col < 150:
            return 2
    elif 50 <= row < 100:
        if 50 <= col < 100:
            return 3
    elif 100 <= row < 150:
        if 0 <= col < 50:
            return 4
        elif 50 <= col < 100:
            return 5
    elif 150 <= row < 200:
        if 0 <= col < 50:
            return 6
    return 0


def move(row, col, mapp, facing, amount):
    while amount > 0:
        oldRow, oldCol, oldFacing = row, col, facing
        currentSection = getSection(row, col)
        if facing == 0:
            col += 1
        elif facing == 1:
            row += 1
        elif facing == 2:
            col -= 1
        elif facing == 3:
            row -= 1
        newSection = getSection(row, col)

        if currentSection != newSection:
            if currentSection == 1:
                if newSection == 0:
                    if facing == 2:  # go from the left to the left of 4
                        facing = 0
                        row = 149 - oldRow
                        col = 0
                    elif facing == 3:  # go from the top to the left of 6
                        facing = 0
                        row = 150 + (oldCol - 50)
                        col = 0
            elif currentSection == 2:
                if newSection == 0:
                    if facing == 0:  # go from the right to the right of 5
                        facing = 2
                        row = 149 - oldRow
                        col = 99
                    elif facing == 1:  # go from the bottom to the right of 3
                        facing = 2
                        row = 50 + (oldCol - 100)
                        col = 99
                    elif facing == 3:  # go from the top to the bottom of 6
                        row = 199
                        col = oldCol - 100
            elif currentSection == 3:
                if newSection == 0:
                    if facing == 0:  # go from the right to the bottom of 2
                        facing = 3
                        row = 49
                        col = 100 + (oldRow - 50)
                    elif facing == 2:  # go from the left to the top of 4
                        facing = 1
                        row = 100
                        col = oldRow - 50
            elif currentSection == 4:
                if newSection == 0:
                    if facing == 2:  # go from the left to the left of 1
                        facing = 0
                        row = 49 - (oldRow - 100)
                        col = 50
                    elif facing == 3:  # go from the top to the left of 3
                        facing = 0
                        row = 50 + oldCol
                        col = 50
            elif currentSection == 5:
                if newSection == 0:
                    if facing == 0:  # go from the right to the right of 2
                        facing = 2
                        row = 49 - (oldRow - 100)
                        col = 149
                    elif facing == 1:  # go from the bottom to the right of 6
                        facing = 2
                        row = 150 + (oldCol - 50)
                        col = 49
            elif currentSection == 6:
                if newSection == 0:
                    if facing == 0:  # go from the right to the bottom of 5
                        facing = 3
                        row = 149
                        col = 50 + (oldRow - 150)
                    elif facing == 1:  # go from the bottom to the top of 2
                        row = 0
                        col = oldCol + 100
                    elif facing == 2:  # go from the left to the top of 1
                        facing = 1
                        row = 0
                        col = 50 + (oldRow - 150)
        if mapp[row][col] == 1:
            return oldRow, oldCol, oldFacing
        amount -= 1
    return row, col, facing


def printMap(mapp, row, col, facing):
    rowIdx = 0
    colIdx = 0
    for r in mapp:
        for c in r:
            if rowIdx == row and colIdx == col:
                if facing == 0:
                    print(">", end="")
                elif facing == 1:
                    print("v", end="")
                elif facing == 2:
                    print("<", end="")
                elif facing == 3:
                    print("^", end="")
            elif c == 2:
                print(" ", end="")
            elif c == 1:
                print("#", end="")
            elif c == 0:
                print(".", end="")
            colIdx += 1
        rowIdx += 1
        colIdx = 0
        print()
    print()


if __name__ == '__main__':
    inputFile = open("input.txt", "r")

    mapp = []
    path = []
    mapping = True
    temp = ""
    maxLength = 0
    for line in inputFile:
        if line == "\n":
            mapping = False
            continue
        if mapping:
            if len(line) > maxLength:
                maxLength = len(line) - 1
            row = []
            for c in line:
                if c == ' ':
                    row.append(2)
                elif c == '#':
                    row.append(1)
                elif c == '.':
                    row.append(0)
            mapp.append(row)
        else:
            for c in line:
                if c == 'R' or c == 'L':
                    path.append(int(temp))
                    path.append(c)
                    temp = ""
                elif c != '\n':
                    temp += c
    if temp != "":
        path.append(int(temp))
    for i in range(len(mapp)):
        if len(mapp[i]) < maxLength:
            mapp[i].extend([2 for j in range(maxLength - len(mapp[i]))])

    facing = 0
    row = 0
    col = 0
    for i in range(len(mapp[0])):
        if mapp[0][i] == 0:
            col = i
            break

    #printMap(mapp, row, col, facing)
    for p in path:
        if p == 'R' or p == 'L':
            facing = rotate(facing, p)
        else:
            row, col, facing = move(row, col, mapp, facing, p)
        #printMap(mapp, row, col, facing)

    print(1000 * (row + 1) + 4 * (col + 1) + facing)

    inputFile.close()
