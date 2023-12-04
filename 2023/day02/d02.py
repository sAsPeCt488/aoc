from math import prod

class CubeSet:
    def __init__(self, red, green, blue):

        self.cubes = [red, green, blue]

    def power(self):
        return prod(self.cubes)

    def __lt__(self, other):
        if isinstance(other, CubeSet):
            return self.cubes < other.cubes
                
        else: 
            return NotImplemented

class Game():

    def __init__(self, game_id, cube_sets):
        self.cube_sets = cube_sets
        self.game_id = game_id

    def get_fewest_possible(self):
        max_set = CubeSet(0, 0, 0)

        for entry in self.cube_sets:
            for i, v in enumerate(max_set.cubes):
                if v < entry.cubes[i]:
                    max_set.cubes[i] = entry.cubes[i]
        return max_set


def parse_game_data(data):
    out = []

    for entry in data.split(";"):
        results = {'red':0, 'green':0, 'blue':0}

        for sub_entry in entry.split(","):
            _, val, color = sub_entry.split(" ")
            results[color] = int(val)

        new_set = CubeSet(*list(results.values()))
        out.append(new_set)

    return out
            
            
def parse_record(record):
    out = []
    for game in record:

        game_header, game_data = game.split(":")
        game_id = int(game_header.split(" ")[1])

        cube_sets = parse_game_data(game_data)
        out.append(Game(game_id, cube_sets))
    return out


PART1_EXAMPLE_ANSWER = 8
PART2_EXAMPLE_ANSWER = 2286


with open("02_example.txt", "r") as f:
    record = [x.strip() for x in f.readlines()]

bag = CubeSet(12, 13, 14)
games = parse_record(record)

part1 = 0
part2 = 0

for game in games:

    max_set = game.get_fewest_possible()
    part2 += max_set.power()

    if max_set < bag:
        part1 += game.game_id

assert part1 == PART1_EXAMPLE_ANSWER, f'Wrong Part 1 answer: {part1} expected {PART1_EXAMPLE_ANSWER}'
assert part2 == PART2_EXAMPLE_ANSWER, f'Wrong Part 2 answer: {part2} expected {PART2_EXAMPLE_ANSWER}'

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")


