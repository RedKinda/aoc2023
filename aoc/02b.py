from collections import defaultdict


day = "02"
input_part = "a"
inp = open("input/{}.txt".format(day)).read()


res = 0

for game in inp.splitlines():
    gamenum, game = game.split(": ")
    gamenum = int(gamenum.split(" ")[1])
    rounds = game.split("; ")

    max_seen = defaultdict(int)

    for round in rounds:
        for d in round.split(", "):
            num, color = d.split(" ")
            max_seen[color] = max(max_seen[color], int(num))

    multiplied = 1
    for color, count in max_seen.items():
        multiplied *= count

    res += multiplied


print(res)
