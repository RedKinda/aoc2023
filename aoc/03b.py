from curses.ascii import isdigit

from .utils import NEIGHBORS_DIAGONAL


day = "03"
input_part = "a"
inp = open("input/{}.txt".format(day)).read()


class Part:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return "Part({})".format(self.val)


mapped = []

for line in inp.splitlines():
    mapped.append([])
    ind = 0
    while ind < len(line):
        c = line[ind]
        if c.isdigit():
            # this is start of a number, find the end
            end = ind + 1
            while end < len(line) and line[end].isdigit():
                end += 1

            num = Part(int(line[ind:end]))
            # append num to mapped N times
            for i in range(end - ind):
                mapped[-1].append(num)

            ind = end
        else:
            mapped[-1].append(c)
            ind += 1


res = 0

# we find all chars non-dots in mapped, and add neighboring parts to res_set
for i in range(len(mapped)):
    for j in range(len(mapped[i])):
        if mapped[i][j] == "*":
            adjacent_parts = set()

            for dx, dy in NEIGHBORS_DIAGONAL:
                x = i + dx
                y = j + dy
                if (
                    0 <= x < len(mapped)
                    and 0 <= y < len(mapped[i])
                    and isinstance(mapped[x][y], Part)
                ):
                    adjacent_parts.add(mapped[x][y])

            if len(adjacent_parts) == 2:
                part1, part2 = list(adjacent_parts)
                res += part1.val * part2.val    


print(res)
