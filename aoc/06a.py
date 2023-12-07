from turtle import distance


day = "06"
inp = open("input/{}.txt".format(day)).read()


times = inp.splitlines()[0][10:].split(" ")
# remove all double spaces
times = [x for x in times if x != ""]
times = list(map(int, times))

distances = inp.splitlines()[1][10:].split(" ")
# remove all double spaces
distances = [x for x in distances if x != ""]
distances = list(map(int, distances))


results = []

for i in range(len(times)):
    time = times[i]
    distance = distances[i]
    ways_to_win = 0

    for chargetime in range(time):
        got_distance = (time - chargetime) * chargetime
        if got_distance > distance:
            ways_to_win += 1

    results.append(ways_to_win)

# multiply all
result = 1
for i in results:
    result *= i

print(result)
