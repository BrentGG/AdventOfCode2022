def resolve(name, names, cont, ops):
    idx = names.index(name)
    if ops[idx] == '':
        return cont[idx]
    else:
        term1 = resolve(cont[idx][0], names, cont, ops)
        term2 = resolve(cont[idx][1], names, cont, ops)
        result = 0
        if ops[idx] == '+':
            result = term1 + term2
        elif ops[idx] == '-':
            result = term1 - term2
        elif ops[idx] == '*':
            result = term1 * term2
        elif ops[idx] == '/':
            result = term1 / term2
        cont[idx] = result
        ops[idx] = ''
        return result


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

    firstName = content[names.index("root")][0]
    secondName = content[names.index("root")][1]
    lower = 0
    higher = -1
    mod = 1
    while True:
        content[names.index("humn")] = lower + mod
        #print(lower + mod, end=": ")
        first = resolve(firstName, names, content.copy(), operations.copy())
        #print(first, end=" ")
        second = resolve(secondName, names, content.copy(), operations.copy())
        #print(second)
        if first == second:
            print("solution: " + str(lower + mod))
            break
        if first > second:
            mod *= 2
        elif first < second:
            #print("------------------------------------------------")
            lower = lower + (mod / 2)
            higher = lower + mod
            mod = 1

    inputFile.close()
