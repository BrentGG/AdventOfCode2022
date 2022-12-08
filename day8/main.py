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

    highestScore = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            score = 1
            viewingDist = 0
            for i in range(row + 1, len(grid)):
                viewingDist += 1
                if grid[i][col] >= grid[row][col]:
                    break
            score *= viewingDist
            viewingDist = 0
            for i in range(row - 1, -1, -1):
                viewingDist += 1
                if grid[i][col] >= grid[row][col]:
                    break
            score *= viewingDist
            viewingDist = 0
            for i in range(col + 1, len(grid[0])):
                viewingDist += 1
                if grid[row][i] >= grid[row][col]:
                    break
            score *= viewingDist
            viewingDist = 0
            for i in range(col - 1, -1, -1):
                viewingDist += 1
                if grid[row][i] >= grid[row][col]:
                    break
            score *= viewingDist
            viewingDist = 0
            if score > highestScore:
                highestScore = score
    print(highestScore)

    inputFile.close()
