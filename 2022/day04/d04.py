
with open("04_input.txt", "r") as input:
    pairs = [[[int(x) for x in n.split('-')]
              for n in line.strip().split(',')] for line in input.readlines()]


def is_contained(pair1, pair2):

    start1, end1 = pair1
    start2, end2 = pair2

    interval1 = set(range(start1, end1 + 1))
    interval2 = set(range(start2, end2 + 1))

    return interval1.issuperset(interval2) or interval1.issubset(interval2)


def do_overlap(pair1, pair2):
    return not (max(pair1) < min(pair2) or max(pair2) < min(pair1))


sum_contained = 0
sum_overlaps = 0

for pair in pairs:

    pair1, pair2 = pair

    if(is_contained(pair1, pair2)):
        sum_contained += 1

    if(do_overlap(pair1, pair2)):
        sum_overlaps += 1

print("Part 1 answer: ", sum_contained)
print("Part 2 answer: ", sum_overlaps)
