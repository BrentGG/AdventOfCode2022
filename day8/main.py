if __name__ == '__main__':
    inputFile = open("input.txt", "r")

    grid = []
    index = 0
    for line in inputFile:
        grid.append([])
        for nr in line:
            if nr != '\n':
                grid[index].append(int(nr))
        index += 1

    visibleTrees = []
    for row in range(1, len(grid) - 1):
        highestInRow = grid[row][0]
        for col in range(1, len(grid[0]) - 1):
            if grid[row][col] > highestInRow:
                highestInRow = grid[row][col]
                visibleTrees.append(str(row) + "," + str(col))
        highestInRow = grid[row][len(grid[row]) - 1]
        for col in range(len(grid[0]) - 2, 0, -1):
            if grid[row][col] > highestInRow:
                highestInRow = grid[row][col]
                visibleTrees.append(str(row) + "," + str(col))
    for col in range(1, len(grid[0]) - 1):
        highestInCol = grid[0][col]
        for row in range(1, len(grid) - 1):
            if grid[row][col] > highestInCol:
                highestInCol = grid[row][col]
                visibleTrees.append(str(row) + "," + str(col))
        highestInCol = grid[len(grid) - 1][col]
        for row in range(len(grid) - 2, 0, -1):
            if grid[row][col] > highestInCol:
                highestInCol = grid[row][col]
                visibleTrees.append(str(row) + "," + str(col))
    visibleTrees = list(set(visibleTrees))
    print(len(visibleTrees) + len(grid) * 2 + len(grid[0]) * 2 - 4)

    inputFile.close()
