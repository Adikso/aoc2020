from aoc_utils import get_input, perf

data = get_input(year=2020, day=9, lines=True, numbers=True)


def part1():
    preamble_len = 25

    for i in range(preamble_len, len(data)):
        number = data[i]
        ranged = data[i - preamble_len:i]
        for preamble_entry in ranged:
            if (number - preamble_entry) in ranged:
                break
        else:
            return number


def part2(invalid):
    total = 0
    start, end = 0, 0
    while end < len(data):
        if total > invalid:
            total -= data[start]
            start += 1
            continue
        elif total < invalid:
            total += data[end]
            end += 1
            continue

        part = data[start:end]
        return min(part) + max(part)


result1, exec_time = perf(part1)
print('Part 1:', result1, exec_time)
print('Part 2:', *perf(part2, result1))
