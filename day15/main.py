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

    y = 2000000
    covered = 0
    for x in range(xMin, xMax + 1):
        for i in range(len(sensors)):
            dist = abs(x - sensors[i][0]) + abs(y - sensors[i][1])
            if dist <= distance[i] and [x, y] not in beacons:
                covered += 1
                break
    print(covered)

    inputFile.close()
