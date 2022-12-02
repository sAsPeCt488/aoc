
with open("02_input.txt", "r") as input:
    guide = [[n for n in round.split(" ")]
             for round in input.read().splitlines()]

score = 0

option_map = {
    'A': 0,
    'B': 1,
    'C': 2,
    'X': 0,
    'Y': 1,
    'Z': 2
}

scoring = [3, 6, 0]

for round in guide:
    op_choice, my_choice = [option_map[choice] for choice in round]

    score += scoring[(my_choice - op_choice) % 3]
    score += my_choice + 1

print("Part 1 answer: ", score)
