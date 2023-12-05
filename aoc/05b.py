from functools import cache
import time
from tracemalloc import start


day = "05"
input_part = "a"
inp = open("input/{}.txt".format(day)).read()


class Mapping:
    __slots__ = ["target", "source", "_range"]

    def __init__(self, target, source, _range):
        self.target = target
        self.source = source
        self._range = _range

    def map(self, num):
        if num >= self.source and num < self.source + self._range:
            return self.target + (num - self.source)

        return None

    def reverse_map(self, num):
        if num >= self.target and num < self.target + self._range:
            return self.source + (num - self.target)

        return None


class Recipe:
    __slots__ = ["mappings"]

    def __init__(self):
        self.mappings = []

    def add_mapping(self, target, source, _range):
        self.mappings.append(Mapping(target, source, _range))

    # @cache
    def revmap(self, num):
        options = []
        base_possible = True
        for mapping in self.mappings:
            if num >= mapping.target and num < mapping.target + mapping._range:
                options.append(mapping.source + (num - mapping.target))

            if num >= mapping.source and num < mapping.source + mapping._range:
                base_possible = False

        if base_possible:
            options.append(num)

        return options


lines = inp.splitlines()

seeds = list(map(int, lines[0][7:].split()))
# seeds are tuples of 2
source_seeds = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]

recipes = []

line_ind = 3
recipe = Recipe()

while line_ind < len(lines):
    line = lines[line_ind]
    if ":" in line:
        recipes.append(recipe)
        recipe = Recipe()
    elif len(line) > 0:
        target, source, _range = map(int, line.split())
        recipe.add_mapping(target, source, _range)

    line_ind += 1

recipes.append(recipe)


start_seed = 4890000
# start_seed = 0
start_time = time.time()

while True:
    if start_seed % 10000 == 0:
        started = start_time
        start_time = time.time()
        throughput = 10000 / (start_time - started)
        print(
            f"testing seed {start_seed} ({throughput} seeds/s)",
        )

    # reverse map the seed
    seeds = [start_seed]
    new_seeds = []

    finished = True

    for recipe in recipes[::-1]:
        for seed in seeds:
            options = []
            base_possible = True
            for mapping in recipe.mappings:
                if seed >= mapping.target and seed < mapping.target + mapping._range:
                    new_seeds.append(mapping.source + (seed - mapping.target))

                if seed >= mapping.source and seed < mapping.source + mapping._range:
                    base_possible = False

            if base_possible:
                new_seeds.append(seed)

        seeds = new_seeds
        new_seeds = []

        if len(seeds) == 0:
            finished = False
            break

    if finished:
        # check if any of the mapped seeds are in the range of the seeds
        for found in seeds:
            for seed in source_seeds:
                if found >= seed[0] and found < seed[0] + seed[1]:
                    # print(found)
                    print(start_seed)
                    exit()

    start_seed += 1
