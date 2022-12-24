def rotate(facing, rotation):
    if rotation == 'R':
        return facing + 1 if facing + 1 <= 3 else 0
    if rotation == 'L':
        return facing - 1 if facing - 1 >= 0 else 3
    return facing


def move(row, col, mapp, facing, amount):
    while amount > 0:
        if facing == 0:
            col += 1
            if col >= len(mapp[row]) or mapp[row][col] == 2:
                for i in range(len(mapp[row])):
                    if mapp[row][i] == 0:
                        col = i
                        break
                    elif mapp[row][i] == 1:
                        return row, col - 1
            elif mapp[row][col] == 1:
                return row, col - 1
        elif facing == 1:
            row += 1
            if row >= len(mapp) or mapp[row][col] == 2:
                for i in range(len(mapp)):
                    if mapp[i][col] == 0:
                        row = i
                        break
                    elif mapp[i][col] == 1:
                        return row - 1, col
            elif mapp[row][col] == 1:
                return row - 1, col
        elif facing == 2:
            col -= 1
            if col < 0 or mapp[row][col] == 2:
                for i in range(len(mapp[row]) - 1, -1, -1):
                    if mapp[row][i] == 0:
                        col = i
                        break
                    elif mapp[row][i] == 1:
                        return row, col - 1
            elif mapp[row][col] == 1:
                return row, col + 1
        else:
            row -= 1
            if row < 0 or mapp[row][col] == 2:
                for i in range(len(mapp) - 1, -1, -1):
                    if mapp[i][col] == 0:
                        row = i
                        break
                    elif mapp[i][col] == 1:
                        return row + 1, col
            elif mapp[row][col] == 1:
                return row + 1, col
        amount -= 1
    return row, col


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

test = 0
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
            row, col = move(row, col, mapp, facing, p)
        #printMap(mapp, row, col, facing)

    print(1000 * (row + 1) + 4 * (col + 1) + facing)

    inputFile.close()
