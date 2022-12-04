
from string import ascii_letters

with open("03_input.txt", "r") as input:
    data = input.read().splitlines(False)
    rucksacks = [data[i:i+3] for i in range(0, len(data), 3)]

sum_priority = 0

for first, second, third in rucksacks:

    common_letter = (set(first) & set(second) & set(third)).pop()
    sum_priority += ascii_letters.find(common_letter) + 1

print("Part 2 answer: ", sum_priority)
