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


def sortPackets(packets):
    if compare(packets[0], packets[1]) == 1:
        sortedPackets = [packets[0], packets[1]]
    else:
        sortedPackets = [packets[1], packets[0]]
    for i in range(2, len(packets)):
        isSorted = False
        for j in range(len(sortedPackets)):
            if compare(packets[i], sortedPackets[j]) == 1:
                sortedPackets.insert(j, packets[i])
                isSorted = True
                break
        if not isSorted:
            sortedPackets.append(packets[i])
    return sortedPackets


if __name__ == '__main__':
    inputFile = open("input.txt", "r")

    packets = [[[2]], [[6]]]
    for line in inputFile:
        if line != "\n":
            packets.append(eval(line))

    packets = sortPackets(packets)

    key = 1
    for i in range(len(packets)):
        if packets[i] == [[2]] or packets[i] == [[6]]:
            key *= i + 1
    print(key)

    inputFile.close()
