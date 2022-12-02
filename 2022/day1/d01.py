
with open("01_input.txt", "r") as input:
    inventory = input.read().splitlines()

elves = []
elf = []

for snack in inventory:
    if not snack:
        elves.append(sum(elf))
        elf.clear()
        continue
    elf.append(int(snack))

max_calories = max(elves)
print(f"Part 1 answer: {max_calories}")

sum_of_3_max = sum(sorted(elves, reverse=True)[0:3])
print(f"Part 2 answer: {sum_of_3_max}")
