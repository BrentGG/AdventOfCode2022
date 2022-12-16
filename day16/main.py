if __name__ == '__main__':
    inputFile = open("testinput.txt", "r")

    valveNames = []
    flowRates = []
    tunnels = []
    for line in inputFile:
        valveNames.append(line[6:8])
        flowRates.append(int(line[line.find("=") + 1:line.find(";")]))
        tempTunnels = []
        if line.find("valves") >= 0:
            prevIndex = line.find("valves") + 7
        else:
            prevIndex = line.rfind("valve") + 6
        while prevIndex < len(line):
            tempTunnels.append(line[prevIndex:prevIndex + 2])
            prevIndex += 4
        tunnels.append(tempTunnels)
    for i in range(len(valveNames)):
        for j in range(len(tunnels[i])):
            tunnels[i][j] = valveNames.index(tunnels[i][j])
            
    inputFile.close()
