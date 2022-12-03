if __name__ == '__main__':
    inputFile = open("input.txt", "r")

    total = 0
    group = []
    for line in inputFile:
        group.append(line[:len(line) - 1])
        if len(group) == 3:
            common = list(set(group[0]).intersection(group[1], group[2]))[0]
            value = ord(common) - 96 if common.islower() else ord(common) - 38
            total += value
            group.clear()
    print(total)

    inputFile.close()
