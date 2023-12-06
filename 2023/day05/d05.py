
with open('05_example.txt', "r") as f:
    almanac = [x.strip() for x in f.readlines() if x.strip()]

PART1_EXAMPLE_ANSWER = 35

def parse_almanac(almanac):

    maps = []
    curr = []

    _, seeds = [x.strip() for x in almanac[0].split(":")]
    seeds = [int(x) for x in seeds.split(" ")]
    almanac.pop(0)
    almanac.pop(0)

    for m in almanac:
        if ":" in m:
            maps.append(curr)
            curr = []
            continue
        curr.append([int(x) for x in m.split(" ")])
    maps.append(curr)
                
    return seeds, maps


def create_mappings(maps):
    out = []
    for m in maps:
        curr = []
        for subm in m:
            dest, src, r = subm
            curr.append((dest, range(src, src + r)))
        out.append(curr)
    return out

def find_min_location(seeds, mappings):
    min_location = 0

    for seed in seeds:
        #print(f"mapping seed {seed}")
        victim = seed
        for m in mappings:
            for subm in m:
                if victim in subm[1]:
                    new = subm[0] + (victim - subm[1].start)
                    victim = new
                    break

        if not min_location or victim < min_location:
            min_location = victim

    return min_location

seeds, maps = parse_almanac(almanac)

mappings = create_mappings(maps)

part1 = find_min_location(seeds, mappings)

assert part1 == PART1_EXAMPLE_ANSWER, f'Wrong Part 1 answer: {part1} expected {PART1_EXAMPLE_ANSWER}'

print(f"Part 1:  {part1}")