import re
with open("Day9.txt", "r") as file:
    lines = file.readlines()

pattern = re.compile("[0-9]+")
final_sum = 0

for line in lines:
    matrix = []
    nums = [int(num) for num in re.findall(pattern, line)]
    matrix.append(nums)
    while not all(num == 0 for num in matrix[-1]):
        temp_nums = []
        for index, n in enumerate(matrix[-1]):
            if index != len(matrix[-1]) - 1:
                temp_nums.append(matrix[-1][index + 1] - n)
    print(matrix)