from math import prod

class CubeSet:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

        self.cubes = [red, green, blue]

    def power(self):
        return prod(self.cubes)

    def __lt__(self, other):
        if isinstance(other, CubeSet):
            return self.red < other.red or \
                self.blue < other.blue or \
                    self.green < other.green
        else: 
            return NotImplemented


class Game():

    def __init__(self, game_id, cube_sets):
        self.cube_sets = cube_sets
        self.game_id = game_id

    def is_possible(self, bag):
        for cubeset in self.cube_sets:
            if bag < cubeset:
                return False
        return True

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



with open("02_example.txt", "r") as f:
    record = [x.strip() for x in f.readlines()]

bag = CubeSet(12, 13, 14)
games = parse_record(record)

part1 = 0
part2 = 0

for game in games:
    
    part2 += game.get_fewest_possible().power()

    if game.is_possible(bag):
        part1 += game.game_id
    
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")


