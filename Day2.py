# Part 1
import re
with open("Day2.txt", "r") as file:
    lines = file.readlines()

RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14

sum_of_games = 0

for line in lines:
    game_pattern = re.compile("Game ([0-9]+):")
    game_num = int(re.findall(game_pattern, line)[0])

    red_cubes_pattern = re.compile("([0-9]+) red")
    green_cubes_pattern = re.compile("([0-9]+) green")
    blue_cubes_pattern = re.compile("([0-9]+) blue")

    red_cubes_nums = re.findall(red_cubes_pattern, line)
    green_cubes_nums = re.findall(green_cubes_pattern, line)
    blue_cubes_nums = re.findall(blue_cubes_pattern, line)
    
    red_check = all(int(num) <= RED_CUBES for num in red_cubes_nums)
    green_check = all(int(num) <= GREEN_CUBES for num in green_cubes_nums)
    blue_check = all(int(num) <= BLUE_CUBES for num in blue_cubes_nums)

    if red_check and green_check and blue_check:
        sum_of_games += game_num

print(sum_of_games)
# 2105


# Part 2

sum_of_power_minimum = 0

for line in lines:
    red_cubes_pattern = re.compile("([0-9]+) red")
    green_cubes_pattern = re.compile("([0-9]+) green")
    blue_cubes_pattern = re.compile("([0-9]+) blue")

    red_cubes_nums = re.findall(red_cubes_pattern, line)
    red_cubes_nums = [int(i) for i in red_cubes_nums]
    red_cubes_num = max(red_cubes_nums)

    green_cubes_nums = re.findall(green_cubes_pattern, line)
    green_cubes_nums = [int(i) for i in green_cubes_nums]
    green_cubes_num = max(green_cubes_nums)

    blue_cubes_nums = re.findall(blue_cubes_pattern, line)
    blue_cubes_nums = [int(i) for i in blue_cubes_nums]
    blue_cubes_num = max(blue_cubes_nums)

    cube_power = red_cubes_num * green_cubes_num * blue_cubes_num
    sum_of_power_minimum += cube_power

print(sum_of_power_minimum)
# 72422