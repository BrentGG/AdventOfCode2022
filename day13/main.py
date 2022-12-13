def stringToList(string, index):
    result = []
    while index < len(string):
        if string[index] == '[':
            temp, index = stringToList(string, index + 1)
            result.append(temp)
        elif string[index] == ']':
            return result, index
        elif string[index] != ',' and string[index] != ' ':
            result.append(int(string[index]))
        index += 1


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
        p1, _ = stringToList(inputFile.readline().replace("\n", ""), 1)
        p2, _ = stringToList(inputFile.readline().replace("\n", ""), 1)
        print(p1)
        print(p2)

        result = compare(p1, p2)
        print("Correct order." if result == 1 else "Incorrect order.")
        if result == 1:
            idxSum += idx
        idx += 1
        print()

        if inputFile.readline() == "":
            break
    print(idxSum)

    inputFile.close()
