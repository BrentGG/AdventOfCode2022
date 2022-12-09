if __name__ == '__main__':
    inputFile = open("input.txt", "r")

    headPos = [0, 0]
    tailPos = [0, 0]
    visited = ["0,0"]
    for line in inputFile:
        moveDirection = line[0]
        moveAmount = int(line[2:])
        while moveAmount > 0:
            if moveDirection == 'U':
                headPos[1] += 1
            elif moveDirection == 'D':
                headPos[1] -= 1
            elif moveDirection == 'L':
                headPos[0] -= 1
            elif moveDirection == 'R':
                headPos[0] += 1
            moveAmount -= 1
            if not(headPos[0] - 1 <= tailPos[0] <= headPos[0] + 1 and headPos[1] - 1 <= tailPos[1] <= headPos[1] + 1):
                if headPos[1] > tailPos[1]:
                    tailPos[1] += 1
                elif headPos[1] < tailPos[1]:
                    tailPos[1] -= 1
                if headPos[0] > tailPos[0]:
                    tailPos[0] += 1
                elif headPos[0] < tailPos[0]:
                    tailPos[0] -= 1
                visited.append(str(tailPos[0]) + "," + str(tailPos[1]))
    print(len(list(set(visited))))

    inputFile.close()
