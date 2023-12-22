# Part 1
import re
with open("Day3.txt", "r") as file:
    lines = file.readlines()

sum = 0
line_count = len(lines)
num_pattern = re.compile("[0-9]+")
gears = {}

for i in range(0, line_count):
   nums = re.findall(num_pattern, lines[i])
   counter = 0
   for num in nums:
        
        num_length = len(num)
        num_index = lines[i].find(num, counter)
        check_spaces = []

        if num_index != 0:
            check_spaces.append(lines[i][num_index - 1])
            if lines[i][num_index - 1] == "*":
                if f"{i},{num_index - 1}" in gears.keys():
                    gears[f"{i},{num_index - 1}"] += ("," + str(num))
                else:
                    gears[f"{i},{num_index - 1}"] = str(num)
        if num_index + num_length != len(lines[i]):
            check_spaces.append(lines[i][num_index + num_length])
            if lines[i][num_index + num_length] == "*":
                if f"{i},{num_index + num_length}" in gears.keys():
                    gears[f"{i},{num_index + num_length}"] += ("," + str(num))
                else:
                    gears[f"{i},{num_index + num_length}"] = str(num)
        if i != 0:
            for j in range(-1, num_length + 1):
                check_spaces.append(lines[i - 1][num_index + j])
                if lines[i - 1][num_index + j] == "*":
                    if f"{i - 1},{num_index + j}" in gears.keys():
                        gears[f"{i - 1},{num_index + j}"] += ("," + str(num))
                    else:
                        gears[f"{i - 1},{num_index + j}"] = str(num)
        if i != line_count - 1:
            for j in range(-1, num_length + 1):
                check_spaces.append(lines[i + 1][num_index + j])
                if lines[i + 1][num_index + j] == "*":
                    if f"{i + 1},{num_index + j}" in gears.keys():
                        gears[f"{i + 1},{num_index + j}"] += ("," + str(num))
                    else:
                        gears[f"{i + 1},{num_index + j}"] = str(num)  

        invalid_num = all(cs == "." or cs == "\n" for cs in check_spaces)
        if not invalid_num:
            sum += int(num)
        counter = num_index + num_length

print(sum)
# 536202


# Part 2

ratio = 0
for key, value in gears.items():
    values = [int(v) for v in value.split(",")]
    if len(values) >= 2:
        temp_ratio = 1
        for v in values:
            temp_ratio *= v
        ratio += temp_ratio

print(ratio)
# 78272573