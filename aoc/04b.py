day = "04"
input_part = "a"
inp = open("input/{}.txt".format(day)).read()


wins = [0 for x in range(inp.count("\n"))]

res = 0
for line in inp.splitlines():
    winning, owned = line.split(":")[1].split("|")

    winning = [int(x) for x in winning.split() if x != " "]
    owned = [int(x) for x in owned.split() if x != " "]

    intersection_count = len(set(winning).intersection(set(owned)))

    copies = wins.pop(0) + 1

    if intersection_count > 0:
        for i in range(intersection_count):
            wins[i] += copies

    print("cards: {}, copies: {}".format(intersection_count, copies))
    res += copies


print(res)
