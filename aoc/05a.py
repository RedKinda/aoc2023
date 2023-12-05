day = "05"
input_part = "a"
inp = open("input/{}.txt".format(day)).read()


class Mapping:
    def __init__(self, target, source, range):
        self.target = target
        self.source = source
        self.range = range

    def map(self, num):
        if num >= self.source and num < self.source + self.range:
            return self.target + (num - self.source)

        return None


class Recipe:
    def __init__(self):
        self.mappings = []

    def add_mapping(self, target, source, range):
        self.mappings.append(Mapping(target, source, range))

    def lowmap(self, num):
        for mapping in self.mappings:
            res = mapping.map(num)
            if res is not None:
                return res

        return num


lines = inp.splitlines()


seeds = list(map(int, lines[0][7:].split()))

recipes = []

line_ind = 3
recipe = Recipe()

while line_ind < len(lines):
    line = lines[line_ind]
    if ":" in line:
        recipes.append(recipe)
        recipe = Recipe()
    elif len(line) > 0:
        target, source, range = map(int, line.split())
        recipe.add_mapping(target, source, range)

    line_ind += 1

recipes.append(recipe)

res_seed = None
for seed in seeds:
    for recipe in recipes:
        mapped = recipe.lowmap(seed)
        print(seed, mapped)
        seed = mapped

    if res_seed is None or seed < res_seed:
        res_seed = seed

print(res_seed)
