import sys

from aoc_utils import get_input

data = get_input(year=2020, day=5, lines=True)


def get_seat_id(code):
    row_from, row_to = 0, 127
    col_from, col_to = 0, 7

    for letter in code:
        if letter == 'F':
            row_to = row_from + (row_to - row_from) // 2
        elif letter == 'B':
            row_from = row_to - (row_to - row_from) // 2
        if letter == 'L':
            col_to = col_from + (col_to - col_from) // 2
        elif letter == 'R':
            col_from = col_to - (col_to - col_from) // 2

    return row_from * 8 + col_from


seats = [get_seat_id(code) for code in data]


def part1():
    return max(seats)


def part2():
    min_seat = min(seats)
    max_seat = max(seats)

    checks = {}
    for seat in seats:
        if seat - 1 not in checks:
            checks[seat - 1] = True
        if seat + 1 not in checks:
            checks[seat + 1] = True

        checks[seat] = False

    for seat, state in checks.items():
        if min_seat <= seat <= max_seat and state:
            return seat

    return None


print('Part 1:', part1())
print('Part 2:', part2())
