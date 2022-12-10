if __name__ == '__main__':
    inputFile = open("input.txt", "r")

    X = 1
    cycle = 1
    wait = 1
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
        currentPos = (cycle % 40) - 1
        print("#" if X - 1 <= currentPos <= X + 1 else ".", end="")
        if cycle % 40 == 0:
            print()
        cycle += 1
        wait -= 1

    inputFile.close()
