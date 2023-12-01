day = "01"
inp = open("input/{}.txt".format(day)).read()

res = 0

for line in inp.splitlines():
    first = None
    for i in range(len(line)):
        if line[i].isdigit():
            first = line[i]
            break

    last = None
    for i in range(len(line)):
        if line[len(line) - i - 1].isdigit():
            last = line[len(line) - i - 1]
            break

    num = int(first) * 10 + int(last)
    print(num)
    res += num


print(res)
