# Part 1
import re
with open("Day4.txt", "r") as file:
    lines = file.readlines()

pattern = re.compile("[0-9]+")
score = 0

for line in lines:
    sets = line.split("|")
    winning_nums = re.findall(pattern, sets[0].split(":")[1])
    my_nums = re.findall(pattern, sets[1])
    
    partial_score = 0
    for num in my_nums:
        if num in winning_nums:
            if partial_score == 0:
                partial_score = 1
            else:
                partial_score *= 2

    score += partial_score

print(score)
# 23750

# Part 2

for i in range(100):
    line = lines[i]
    sets = line.split("|")
    winning_nums = re.findall(pattern, sets[0].split(":")[1])
    my_nums = re.findall(pattern, sets[1])
    wins = 0
    for num in my_nums:
        if num in winning_nums:
            wins += 1
    for j in range(wins):
        lines.insert(i + 1 + 2 * j, lines[i + j + 1])
print(len(lines))


