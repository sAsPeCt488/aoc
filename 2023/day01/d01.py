
with open("01_example_p1.txt", "r") as f:
    data_p1 = [x.strip() for x in f.readlines()]

with open("01_example_p2.txt", "r") as f:
    data_p2 = [x.strip() for x in f.readlines()]

num_map = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
}


def find_all(haystack, needle):
    start = 0
    while True:
        start = haystack.find(needle, start)
        if start == -1: return
        yield start
        start += 1 


def fetch_word_nums(line):
    results = []
    for k, v in  num_map.items():
        idxes = find_all(line, k)
        for idx in idxes:
            if idx >= 0:
                results.append((idx, v))
    return results

def recover_value(line, ignore_words=True):

    nums = [(i, c) for i, c in enumerate(line) if c.isnumeric()]

    if not ignore_words:
        for elem in fetch_word_nums(line):
            nums.append(elem)

    sorted_nums = sorted(nums, key=lambda k: k[0])
    if len(sorted_nums) < 2:
        _, num = sorted_nums[0]
        return int(num * 2)
    else:
        _, num1 = sorted_nums[0]
        _, num2 = sorted_nums[-1]
        return int(num1 + num2)

part1 = 0
part2 = 0

for line in data_p1:
    part1 += recover_value(line)

for line in data_p2:
    part2 += recover_value(line, ignore_words=False)

print(part1, part2)