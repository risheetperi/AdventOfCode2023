# Part 1
import re
import sys
with open("Day8.txt", "r") as file:
    lines = file.readlines()

left_nodes = {}
right_nodes = {}

left_node_pattern = re.compile("\(([A-Z]+),")
right_node_patterm = re.compile(", ([A-Z]+)\)")

directions = lines[0].strip()
node_map = lines[2:]

# for Part 2
part2_nodes = []

for line in node_map:
    parts = line.split(" = ")
    node = parts[0].strip()
    left_node = re.findall(left_node_pattern, parts[1])[0]
    right_node = re.findall(right_node_patterm, parts[1])[0]
    # For Part 2
    if node[-1] == "A":
        part2_nodes.append(node)

    if node not in left_nodes.keys():
        left_nodes[node] = left_node
    if node not in right_nodes.keys():
        right_nodes[node] = right_node

steps = 0
current_node = "AAA"
end_node = "ZZZ"
# while True:
#     for direction in directions:
#         if direction == "L":
#             current_node = left_nodes[current_node]
#         elif direction == "R":
#             current_node = right_nodes[current_node]
#         steps += 1
#         if current_node == end_node:
#             print(steps)
#             sys.exit("Found number of steps")

# 11567

print(part2_nodes)
# Part 2
while True:
    for direction in directions:
        temp_list = part2_nodes[:]
        for node in temp_list:    
            if direction == "L":
                temp_index = part2_nodes.index(node)
                node = left_nodes[node]
                part2_nodes.pop(temp_index)
                part2_nodes.insert(temp_index, node)
            elif direction == "R":
                temp_index = part2_nodes.index(node)
                node = right_nodes[node]
                part2_nodes.pop(temp_index)
                part2_nodes.insert(temp_index, node)
        steps += 1
        print(part2_nodes)
        print(steps)

        if all(node[-1] == "Z" for node in part2_nodes):
            print(steps)
            sys.exit("Found number of steps")    

