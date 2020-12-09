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


def part2(expected):
    total = 0
    from_pos, to_pos = 0, 0
    while from_pos != len(data) and to_pos != len(data):
        if total > expected:
            total -= data[from_pos]
            from_pos += 1
        elif total < expected:
            total += data[to_pos]
            to_pos += 1
        elif to_pos - from_pos > 1:
            part = data[from_pos:to_pos]
            return min(part) + max(part)


result1, exec_time = perf(part1)
print('Part 1:', result1, exec_time)
print('Part 2:', *perf(part2, result1))
