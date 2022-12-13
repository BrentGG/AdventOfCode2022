def compare(p1, p2):
    idx = 0
    while True:
        if idx >= len(p1) and idx < len(p2):
            return 1
        elif idx < len(p1) and idx >= len(p2):
            return -1
        elif idx >= len(p1) and idx >= len(p2):
            return 0
        if not isinstance(p1[idx], list) and not isinstance(p2[idx], list):
            if p1[idx] < p2[idx]:
                return 1
            elif p1[idx] > p2[idx]:
                return -1
        elif not isinstance(p1[idx], list) and isinstance(p2[idx], list):
            result = compare([p1[idx]], p2[idx])
            if result != 0:
                return result
        elif isinstance(p1[idx], list) and not isinstance(p2[idx], list):
            result = compare(p1[idx], [p2[idx]])
            if result != 0:
                return result
        else:
            result = compare(p1[idx], p2[idx])
            if result != 0:
                return result
        idx += 1


if __name__ == '__main__':
    inputFile = open("input.txt", "r")

    idx = 1
    idxSum = 0
    while True:
        p1 = eval(inputFile.readline())
        p2 = eval(inputFile.readline())
        if compare(p1, p2) == 1:
            idxSum += idx
        idx += 1
        if inputFile.readline() == "":
            break
    print(idxSum)

    inputFile.close()
