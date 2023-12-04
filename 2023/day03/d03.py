import re
from math import prod

with open('03_example.txt', "r") as f:
    schematic = [line.strip() for line in f.readlines()]


COLUMNS = len(schematic[0])
ROWS = len(schematic)

PART1_EXAMPLE_ANSWER = 4361
PART2_EXAMPLE_ANSWER = 467835


def find_symbols(schematic: list[str], only_gears=False):

    symbols = []
    pattern = re.compile(r'[^a-zA-Z0-9\s.]')
    
    for i, line in enumerate(schematic):
        matches = pattern.finditer(line)
        if matches:
            symbols.extend([(i, match.start(), match.group() == '*') for match in matches])

    return symbols


def search_range(schematic, symbol: tuple, radius = 1):

    numbers = []
    row, col, is_gear = symbol

    for i in range(row - radius, row + radius + 1):
        for j in range(col - radius, col + radius + 1):
            if(i == row and j == col):
                continue

            if schematic[i][j].isdigit():
                numbers.append((i, j))
    return numbers

def recover_number(schematic, point: tuple):
    i, j = point

    start = j
    while((start - 1 >= 0) and schematic[i][start - 1].isdigit()):
        start -= 1

    end = j
    while((end + 1 < COLUMNS) and schematic[i][end + 1].isdigit()):
        end += 1

    return (i, start, end)


def fetch_nums(schematic, num_ranges: set):
    out = []
    for r in num_ranges:
        i, start, end = r
        out.append(int(schematic[i][start:end+1]))
    return out

print(f"Schematic is {ROWS}x{COLUMNS}")

syms = find_symbols(schematic)

number_points = []
number_points_gears = []
numbers = set()
gear_nums = set()

part2 = 0

for sym in syms:
    nums = search_range(schematic, sym)
    number_points.extend(nums)
    if sym[2]:
        gear_nums = set()
        for num in nums:
            gear_nums.add(recover_number(schematic, num))
        if len(gear_nums) == 2:
            part2 += prod(fetch_nums(schematic, gear_nums))
    
for point in number_points:
    numbers.add(recover_number(schematic, point))

part1 = sum(fetch_nums(schematic, numbers))

assert part1 == PART1_EXAMPLE_ANSWER, f'Wrong Part 1 answer: {part1} expected {PART1_EXAMPLE_ANSWER}'
assert part2 == PART2_EXAMPLE_ANSWER, f'Wrong Part 2 answer: {part2} expected {PART2_EXAMPLE_ANSWER}'

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")