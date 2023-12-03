from collections import defaultdict


day = "02"
input_part = "a"
inp = open("input/{}.txt".format(day)).read()

LIMIT = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


good_ids = []

for game in inp.splitlines():
    gamenum, game = game.split(": ")
    gamenum = int(gamenum.split(" ")[1])
    rounds = game.split("; ")

    max_seen = defaultdict(int)

    for round in rounds:
        for d in round.split(", "):
            num, color = d.split(" ")
            max_seen[color] = max(max_seen[color], int(num))

    # check if max_seen exceeds LIMIT
    if all(max_seen[color] <= LIMIT[color] for color in LIMIT):
        print("No illegal moves")
        good_ids.append(gamenum)
    else:
        print("Illegal moves")

print(sum(good_ids))
