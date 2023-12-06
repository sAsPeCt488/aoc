from numpy import sqrt

with open('06_example.txt', 'r') as f:
    race_sheet = [x.strip() for x in f.readlines() if x.strip()]

PART1_EXAMPLE_ANSWER = 288
PART2_EXAMPLE_ANSWER = 71503

def parse_race_sheet(race_sheet):
    out = []
    time_data = [int(x.strip()) for x in race_sheet[0].split(":")[1].split(" ") if x.strip()]
    distance_data = [int(x.strip()) for x in race_sheet[1].split(":")[1].split(" ") if x.strip()]
    return list(zip(time_data, distance_data))

def get_win_combs(race):
    time, record = race

    D = (time**2 - 4 * (record))
    x1 = (time - sqrt(D)) // 2
    x2 = (time + sqrt(D)) // 2

    if(x1 % 2 == 0 and x2 % 2 == 0):
        return int(x2 - x1 - 1)
    return int(x2 - x1)

def create_race_part2(data):
    time = ''
    distance = ''
    for race in data:
        t, d = race
        time += str(t)
        distance += str(d)
    return (int(time), int(distance))

data = parse_race_sheet(race_sheet)

part1 = 1

for race in data:
    part1 *= get_win_combs(race)


race_part_2 = create_race_part2(data)
part2 = get_win_combs(race_part_2)

assert part1 == PART1_EXAMPLE_ANSWER, f'Wrong Part 1 answer: {part1} expected {PART1_EXAMPLE_ANSWER}'
assert part2 == PART2_EXAMPLE_ANSWER, f'Wrong Part 2 answer: {part2} expected {PART2_EXAMPLE_ANSWER}'

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")