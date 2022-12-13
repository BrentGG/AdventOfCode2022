def searchMin(distance, unvisited):
    minPos = unvisited[0]
    for pos in unvisited:
        if distance[pos[0]][pos[1]] < distance[minPos[0]][minPos[1]]:
            minPos = pos
    return minPos


def isNeighbour(heightMap, neighbour, pos, unvisited):
    if neighbour not in unvisited:
        return False
    if neighbour[0] < 0 or neighbour[0] >= len(heightMap) or neighbour[1] < 0 or neighbour[1] >= len(heightMap[0]):
        return False
    if heightMap[neighbour[0]][neighbour[1]] > heightMap[pos[0]][pos[1]] + 1:
        return False
    return True


def getNeighbours(heightMap, pos, unvisited):
    neighbours = []
    if isNeighbour(heightMap, [pos[0] - 1, pos[1]], pos, unvisited):  # move up
        neighbours.append([pos[0] - 1, pos[1]])
    if isNeighbour(heightMap, [pos[0] + 1, pos[1]], pos, unvisited):  # move down
        neighbours.append([pos[0] + 1, pos[1]])
    if isNeighbour(heightMap, [pos[0], pos[1] - 1], pos, unvisited):  # move left
        neighbours.append([pos[0], pos[1] - 1])
    if isNeighbour(heightMap, [pos[0], pos[1] + 1], pos, unvisited):  # move right
        neighbours.append([pos[0], pos[1] + 1])
    return neighbours


def dijkstra(heightMap, source, target):
    distance = []
    previous = []
    unvisited = []
    for i in range(len(heightMap)):
        distance.append([])
        previous.append([])
        for j in range(len(heightMap[0])):
            distance[i].append(999999)
            previous[i].append(None)
            unvisited.append([i, j])
    distance[source[0]][source[1]] = 0

    while len(unvisited) > 0:
        current = searchMin(distance, unvisited)
        if current == target:
            break
        unvisited.remove(current)
        for neighbour in getNeighbours(heightMap, current, unvisited):
            newDist = distance[current[0]][current[1]] + 1
            if newDist < distance[neighbour[0]][neighbour[1]]:
                distance[neighbour[0]][neighbour[1]] = newDist
                previous[neighbour[0]][neighbour[1]] = current

    return distance, previous


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

    dist, prev = dijkstra(heightMap, start, end)
    print(dist[end[0]][end[1]])

    inputFile.close()
