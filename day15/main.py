def updateBounds(xMin, xMax, yMin, yMax, xNew, yNew):
    if xNew < xMin:
        xMin = xNew
    if xNew > xMax:
        xMax = xNew
    if yNew < yMin:
        yMin = yNew
    if yNew > yMax:
        yMax = yNew
    return xMin, xMax, yMin, yMax


def sortCovered(covered, reverse):
    newCovered = [covered[0]]
    for i in range(1, len(covered)):
        sorted = False
        for j in range(len(newCovered)):
            if not reverse:
                if covered[i][0] < newCovered[j][0]:
                    newCovered.insert(j, covered[i])
                    sorted = True
                    break
            else:
                if covered[i][1] > newCovered[j][1]:
                    newCovered.insert(j, covered[i])
                    sorted = True
                    break
        if not sorted:
            newCovered.append(covered[i])
    return newCovered


def isFullyCovered(min, max, covered):
    covered = sortCovered(covered, False)
    if covered[0][0] > min:
        return False, min
    tempMax = covered[0][1]
    for i in range(len(covered) - 1):
        if covered[i + 1][0] > tempMax:
            return False, covered[i][1] + 1
        if covered[i + 1][1] > tempMax:
            tempMax = covered[i + 1][1]
    if tempMax < max:
        return False, max
    return True, None


if __name__ == '__main__':
    inputFile = open("input.txt", "r")

    sensors = []
    beacons = []
    distance = []
    xMin, xMax = 0, 0
    yMin, yMax = 0, 0
    for line in inputFile:
        sensX = int(line[line.find("x=") + 2:line.find(",")])
        sensY = int(line[line.find("y=") + 2:line.find(":")])
        sensors.append([sensX, sensY])
        xMin, xMax, yMin, yMax = updateBounds(xMin, xMax, yMin, yMax, sensX, sensY)
        line = line[line.find(":"):]
        beacX = int(line[line.find("x=") + 2:line.find(",")])
        beacY = int(line[line.find("y=") + 2:])
        beacons.append([beacX, beacY])
        xMin, xMax, yMin, yMax = updateBounds(xMin, xMax, yMin, yMax, beacX, beacY)
        dist = abs(beacX - sensX) + abs(beacY - sensY)
        distance.append(dist)
        xMin, xMax, yMin, yMax = updateBounds(xMin, xMax, yMin, yMax, sensX + dist, sensY)
        xMin, xMax, yMin, yMax = updateBounds(xMin, xMax, yMin, yMax, sensX, sensY + dist)

    tuningFreq = 0
    min, max = 0, 4000000
    for y in range(min, max + 1):
        covered = []
        for i in range(len(sensors)):
            distToSpare = distance[i] - abs(sensors[i][1] - y)
            if distToSpare >= 0:
                covered.append([sensors[i][0] - distToSpare, sensors[i][0] + distToSpare])
        isCovered, freeX = isFullyCovered(min, max, covered)
        if not isCovered:
            tuningFreq = freeX * 4000000 + y
            break
    print(tuningFreq)

    inputFile.close()
