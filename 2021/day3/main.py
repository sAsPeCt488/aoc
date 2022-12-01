
with open("03_input.txt", "r") as input:
    data = [num for num in input.read().splitlines()]


NUM_SIZE = len(data[0])


def part1():
    def findMostCommonBit(pos):
        result = 0
        for num in data:
            result += int(num[pos])
        if result/len(data) > 0.5:
            return '1'
        else:
            return '0'

    gamma_rate = ''
    for i in range(0, NUM_SIZE):
        gamma_rate += findMostCommonBit(i)

    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = gamma_rate ^ int((b'0b' + b'1' * NUM_SIZE), 2)

    return epsilon_rate * gamma_rate


def part2():
    def findMostCommonBit(pos, data):
        result = 0
        for num in data:
            result += int(num[pos])
        if (result / len(data)) >= 0.5:
            return '1'
        else:
            return '0'

    def invertBit(bit):
        return '0' if bit == '1' else '1'

    def filterData(pos, value, data):
        filtered = []
        for num in data:
            if num[pos] == value:
                filtered.append(num)
        return filtered

    def findValue(data, mostCommon):
        for i in range(NUM_SIZE):
            if len(data) == 1:
                break
            commonbit = findMostCommonBit(
                i, data) if mostCommon else invertBit(findMostCommonBit(i, data))
            data = filterData(
                i, commonbit,  data)
        return data[0]

    o2_gen_rate = findValue(data, mostCommon=True)
    co2_scrub_rate = findValue(data, mostCommon=False)
    life_supp_rate = int(o2_gen_rate, 2) * int(co2_scrub_rate, 2)

    return life_supp_rate


print("[+] Part 1 - Result: ", part1())
print("[+] Part 2 - Result: ", part2())
