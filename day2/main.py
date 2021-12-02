
with open("02_input.txt", "r") as input:
    commands = [command for command in input.read().splitlines()]


def part1():
    horizontal = 0
    depth = 0

    for command in commands:
        command, units = command.split(' ')
        if command == 'forward':
            horizontal += int(units)
        elif command == 'up':
            depth -= int(units)
        else:
            depth += int(units)
    return horizontal * depth


def part2():
    horizontal = 0
    depth = 0
    aim = 0

    for command in commands:
        command, units = command.split(' ')
        if command == 'forward':
            horizontal += int(units)
            depth += aim * int(units)
        elif command == 'up':
            aim -= int(units)
        else:
            aim += int(units)

    return horizontal * depth


print("[+] Part 1 - Result: ", part1())
print("[+] Part 1 - Result: ", part2())
