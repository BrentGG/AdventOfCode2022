if __name__ == '__main__':
    inputFile = open("input.txt", "r")

    marker = []
    index = 1
    for char in inputFile.read():
        marker.append(char)
        if len(marker) < 14:
            index += 1
            continue
        if len(marker) > 14:
            marker.pop(0)
        if len(marker) == len(set(marker)):
            break
        index += 1
    print(index)
    inputFile.close()
