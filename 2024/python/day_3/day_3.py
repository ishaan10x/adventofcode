import re

with open("day_3/input.txt") as file:
    data = file.read()

# Part 1 Logic:
def compute_valid_1(data):
    return sum(int(j) * int(k) for j, k in re.findall(r"mul\((\d+),(\d+)\)", data))

# Part 2 Logic
def compute_valid_2(data):
    result = 0
    is_enabled = True

    for command, j, k in re.findall("(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", data):
        if command == "do()":
            is_enabled = True
        elif command == "don't()":
            is_enabled = False
        elif is_enabled and command.startswith("mul("):
            result += int(j) * int(k)

    return result

# Part 1 Answer:
print(compute_valid_1(data))

# Part 2 Answer:
print(compute_valid_2(data))