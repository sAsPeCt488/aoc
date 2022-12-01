with open("01_input.txt", "r") as input:
    calories = input.read().splitlines()

elves = []
elf = []
for n in calories:
    if not n:
        elves.append(sum(elf))
        elf.clear()
        continue
    elf.append(int(n))

max_calories = max(elves)
print(f"Part 1 answer: {max_calories}")

sum_of_3_max = sum(sorted(elves, reverse=True)[0:3])
print(f"Part 2 answer: {sum_of_3_max}")
