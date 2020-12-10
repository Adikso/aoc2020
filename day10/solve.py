from collections import defaultdict
from aoc_utils import get_input, perf

data = get_input(year=2020, day=10, lines=True, numbers=True)
data = sorted(data)


def part1():
    diffs = defaultdict(int)
    diffs[3] += 1
    for i in range(len(data)):
        if i == 0:
            diffs[data[i]] += 1
        else:
            diffs[data[i] - data[i - 1]] += 1

    return diffs[1] * diffs[3]


def part2():
    last, ones = 0, 0
    value = 1
    for i, num in enumerate(data):
        if num - last == 1:
            ones += 1

        if num - last == 3 or i == len(data) - 1:
            if ones == 2:
                value *= 2
            elif ones == 3:
                value *= 4
            elif ones == 4:
                value *= 7

            ones = 0

        last = num

    return value


print('Part 1:', perf(part1))
print('Part 2:', perf(part2))
