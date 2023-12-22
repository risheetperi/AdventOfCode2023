# Part 1
import re

with open("Day1.txt", "r") as file:
    lines = file.readlines()

sum = 0
pattern = re.compile("[0-9]")
for line in lines:
    digits = re.findall(pattern, line)
    num = int(digits[0]) * 10 + int(digits[-1])
    sum += num
print(sum)
# 56108


# Part 2
digits_dict = {'zero' : 0, 'one' : 1, 'two' : 2,
               'three' : 3, 'four' : 4, 'five' : 5,
               'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}

sum = 0
pattern = re.compile("[0-9]|zero|one|two|three|four|five|six|seven|eight|nine")
for line in lines:
    digits = []
    for l in line:
        try:
            digit = re.findall(pattern, line)[0]
        except:
            break
        if not digit.isdigit():
            digit = digits_dict[digit]
        digits.append(digit)
        line = line[1:]
    num = int(digits[0]) * 10 + int(digits[-1])
    sum += num
print(sum)
# 55652