if __name__ == '__main__':
    inputFile = open("input.txt", "r")

    X = 1
    cycle = 1
    wait = 1
    count = 1
    signalSum = 0
    line = inputFile.readline()
    if line[:4] == "noop":
        wait = 1
    elif line[:4] == "addx":
        wait = 2
    while line != "":
        if wait == 0:
            if line[:4] == "addx":
                X += int(line[5:])
            line = inputFile.readline()
            if line[:4] == "noop":
                wait = 1
            elif line[:4] == "addx":
                wait = 2
        if cycle == 20 or count == 40:
            signalSum += cycle * X
            count = 0
            print("cycle nr = " + str(cycle))
        if cycle >= 20:
            count += 1
        cycle += 1
        wait -= 1
    print(signalSum)

    inputFile.close()
