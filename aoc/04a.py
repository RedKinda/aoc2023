day = "04"
input_part = "a"
inp = open("input/{}.txt".format(day)).read()


res = 0
for line in inp.splitlines():
    winning, owned = line.split(":")[1].split("|")

    winning = [int(x) for x in winning.split() if x != " "]
    owned = [int(x) for x in owned.split() if x != " "]

    value = 0.5

    intersection_count = len(set(winning).intersection(set(owned)))
    for i in range(intersection_count):
        value *= 2

    if value >= 1:
        res += int(value)


print(res)
