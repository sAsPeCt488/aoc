import copy

with open("05_example.txt") as input:
    data = input.readlines()


def move_crate(dest, src, n):
    for i in range(n):
        stacks[dest].append(stacks[src].pop())


def move_crate2(dest, src, n):
    tmp = []
    for i in range(n):
        tmp.append(stacks2[src].pop())
    tmp.reverse()
    for crate in tmp:
        stacks2[dest].append(crate)


n_of_stacks = (len(data[0]) // 4)

stacks = [list() for _ in range(n_of_stacks)]

crates = [list() for _ in range(n_of_stacks)]

moves = []

for i in range(n_of_stacks):
    for j in range(0, len(data[i]), 4):
        crates[i].append(data[i][j:j + 4])

for i in range(n_of_stacks):
    for j in range(n_of_stacks):
        if(crates[i][j] != '    '):
            stacks[j].append(crates[i][j].strip())

for i in range(n_of_stacks):
    stacks[i].reverse()

stacks2 = copy.deepcopy(stacks)

for line in data[n_of_stacks + 1:]:
    moves.append([int(line.strip().split(' ')[i]) for i in range(1, 7, 2)])


for move in moves:
    n, src, dest = move
    move_crate(dest - 1, src - 1, n)
    move_crate2(dest - 1, src - 1, n)

print("Part 1 answer: ", "".join([stack[-1].replace('[', '').replace(']', '')
                                  for stack in stacks]))

print("Part 2 answer: ", "".join([stack[-1].replace('[', '').replace(']', '')
                                  for stack in stacks2]))
