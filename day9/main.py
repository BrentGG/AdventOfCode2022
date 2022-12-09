if __name__ == '__main__':
    inputFile = open("input.txt", "r")

    nodes = []
    for i in range(10):
        nodes.append([0, 0])
    visited = ["0,0"]
    for line in inputFile:
        moveDirection = line[0]
        moveAmount = int(line[2:])
        while moveAmount > 0:
            if moveDirection == 'U':
                nodes[0][1] += 1
            elif moveDirection == 'D':
                nodes[0][1] -= 1
            elif moveDirection == 'L':
                nodes[0][0] -= 1
            elif moveDirection == 'R':
                nodes[0][0] += 1
            moveAmount -= 1
            for i in range(1, len(nodes)):
                if not(nodes[i - 1][0] - 1 <= nodes[i][0] <= nodes[i - 1][0] + 1 and nodes[i - 1][1] - 1 <= nodes[i][1] <= nodes[i - 1][1] + 1):
                    if nodes[i - 1][1] > nodes[i][1]:
                        nodes[i][1] += 1
                    elif nodes[i - 1][1] < nodes[i][1]:
                        nodes[i][1] -= 1
                    if nodes[i - 1][0] > nodes[i][0]:
                        nodes[i][0] += 1
                    elif nodes[i - 1][0] < nodes[i][0]:
                        nodes[i][0] -= 1
            visited.append(str(nodes[len(nodes) - 1][0]) + "," + str(nodes[len(nodes) - 1][1]))
    print(len(list(set(visited))))

    inputFile.close()
