def resolve(name, names, content, operations):
    idx = names.index(name)
    if operations[idx] == '':
        return content[idx]
    else:
        term1 = resolve(content[idx][0], names, content, operations)
        term2 = resolve(content[idx][1], names, content, operations)
        if operations[idx] == '+':
            content[idx] = term1 + term2
            return term1 + term2
        elif operations[idx] == '-':
            content[idx] = term1 - term2
            return term1 - term2
        elif operations[idx] == '*':
            content[idx] = term1 * term2
            return term1 * term2
        elif operations[idx] == '/':
            content[idx] = term1 / term2
            return term1 / term2


if __name__ == '__main__':
    inputFile = open("input.txt", "r")

    names = []
    content = []
    operations = []
    for line in inputFile:
        names.append(line[:4])
        if line[6].isnumeric():
            content.append(int(line[6:]))
            operations.append('')
        else:
            content.append([line[6:10], line[13:17]])
            operations.append(line[11])

    print(resolve("root", names, content, operations))

    inputFile.close()
