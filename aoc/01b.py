day = "01"
inp = open("input/{}.txt".format(day)).read()

res = 0

MAP = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

for line in inp.splitlines():
    first = None
    for i in range(len(line)):
        if line[i].isdigit():
            first = line[i]
            break
        for key in MAP:
            if line[i : i + len(key)] == key:
                first = MAP[key]
                break
        if first is not None:
            break

    last = None
    for i in range(len(line)):
        if line[len(line) - i - 1].isdigit():
            last = line[len(line) - i - 1]
            break
        for key in MAP:
            if line[len(line) - i - 1 :].startswith(key):
                last = MAP[key]
                break
        if last is not None:
            break

    num = int(first) * 10 + int(last)
    print(num)
    res += num


print(res)
