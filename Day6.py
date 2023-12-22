# Part 1
with open("Day6.txt", "r") as file:
    lines = file.readlines()

import re
pattern = re.compile("[0-9]+")

times = [int(t) for t in re.findall(pattern, lines[0])]
distances = [int(t) for t in re.findall(pattern, lines[1])]
margin_of_error = 1

for i, time in enumerate(times):
    temp_moe = 0
    for t in range(time):
        way_to_win = (time - t) * t > distances[i]
        if way_to_win:
            temp_moe += 1
    margin_of_error *= temp_moe

print(margin_of_error)
# 2374848


# Part 2
time = int(lines[0].split(":")[1].replace(" ",""))
distance = int(lines[1].split(":")[1].replace(" ",""))

moe = 0
for t in range(time):
    way_to_win = (time - t) * t > distance
    if way_to_win:
        moe += 1

print(moe)
# 39132886