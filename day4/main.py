if __name__ == '__main__':
    inputFile = open("input.txt", "r")

    count = 0
    for line in inputFile:
        first = line[:line.find(",")]
        second = line[line.find(",") + 1:]
        firstBegin = int(first[:first.find("-")])
        firstEnd = int(first[first.find("-") + 1:])
        secondBegin = int(second[:second.find("-")])
        secondEnd = int(second[second.find("-") + 1:])
        if (secondBegin <= firstBegin <= secondEnd) or (secondBegin <= firstEnd <= secondEnd) or (firstBegin <= secondBegin <= firstEnd) or (firstBegin <= secondEnd <= firstEnd):
            count += 1
    print(count)

    inputFile.close()
