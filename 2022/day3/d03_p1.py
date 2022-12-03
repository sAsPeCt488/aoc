
from string import ascii_letters

with open("03_input.txt", "r") as input:
    rucksacks = [rucksack.strip() for rucksack in input.readlines()]

sum_priority = 0

for rucksack in rucksacks:

    first = rucksack[:(len(rucksack)//2)]
    second = rucksack[(len(rucksack)//2):]

    common_letter = (set(first) & set(second)).pop()
    sum_priority += ascii_letters.find(common_letter) + 1

print("Part 1 answer: ", sum_priority)
