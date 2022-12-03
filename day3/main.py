if __name__ == '__main__':
    inputFile = open("input.txt", "r")

    total = 0
    for line in inputFile:
        length = len(line) - 1
        comp1 = line[:int(length / 2)]
        comp2 = line[int(length / 2):]
        common = list(set(comp1).intersection(comp2))[0]
        value = ord(common) - 96 if common.islower() else ord(common) - 38
        total += value
    print(total)

    inputFile.close()
