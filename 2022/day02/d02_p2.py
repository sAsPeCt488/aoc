
with open("02_input.txt", "r") as input:
    guide = [[n for n in round.split(" ")]
             for round in input.read().splitlines()]

score = 0

option_map = {
    'A': 0,
    'B': 1,
    'C': 2,
    'X': -1,
    'Y': 0,
    'Z': 1
}

scoring = [3, 6, 0]

for round in guide:
    op_choice, round_res = [option_map[choice] for choice in round]

    my_choice = (op_choice + round_res) % 3
    score += (round_res + 1) * 3
    score += my_choice + 1

print("Part 2 answer: ", score)
