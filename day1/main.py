
with open("input.txt", "r") as input:
    measurements = [int(num) for num in input.read().splitlines()]


def part1():
    inc_counter = 0
    for i in range(1, len(measurements)):
        if measurements[i-1] < measurements[i]:
            inc_counter += 1
    return inc_counter


def part2():
    inc_counter = 0
    for i in range(len(measurements) - 3):
        if measurements[i] < measurements[i + 3]:
            inc_counter += 1
    return inc_counter


print("[+] Part 1  - Result: ", part1())
print("[+] Part 2  - Result: ", part2())
