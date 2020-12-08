from aoc_utils import get_input

data = get_input(
    year=2020,
    day=3,
    lines=True
)


def part1(slope):
    x_off, y_off = slope
    x, y = 0, 0

    trees_count = 0
    while y < len(data):
        if data[y][x % len(data[0])] == '#':
            trees_count += 1

        x += x_off
        y += y_off

    return trees_count


def part2():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    result = 1
    for slope in slopes:
        result *= part1(slope)

    return result


print('Part 1:', part1((3, 1)))
print('Part 2:', part2())
