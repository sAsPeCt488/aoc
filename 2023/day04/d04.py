
with open('04_example.txt', 'r') as f:
    scratch_cards = [line.strip() for line in f.readlines()]

PART1_EXAMPLE_ANSWER = 13
PART2_EXAMPLE_ANSWER = 30


def parse_scratchcard(card):
    header, body = card.split(":")
    winners, own_numbers = body.split("|")

    winners = [int(x) for x in winners.split(" ") if x]
    own_numbers = [int(x) for x in own_numbers.split(" ") if x]

    return set(winners), set(own_numbers)

def get_matches(winners, own_numbers):
    return len(winners & own_numbers)

def calculate_points(matches, winners, own_nums):
    if matches:
        return 2**(matches - 1)
    return 0

part1 = 0
 
part2 = [1] * len(scratch_cards)


for i, card in enumerate(scratch_cards):
    winners, own = parse_scratchcard(card)
    matches = get_matches(winners, own)

    for j in range(i + 1, i + 1 + matches):
        part2[j] += part2[i]

    part1 += calculate_points(matches, winners, own)

assert part1 == PART1_EXAMPLE_ANSWER, f'Wrong Part 1 answer: {part1} expected {PART1_EXAMPLE_ANSWER}'
assert part2 == PART2_EXAMPLE_ANSWER, f'Wrong Part 2 answer: {part2} expected {PART2_EXAMPLE_ANSWER}'

print(f"Part 1: {part1}")
print(f"Part 2: {sum(part2)}")