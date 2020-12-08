from time import perf_counter

from aoc_utils import get_input
from z3 import *

data = get_input(2020, 1, lines=True, numbers=True)


def part1():
    s = Solver()
    x, y, result = Ints("x y result")

    s.add(Or(*[x == val for val in data]))
    s.add(Or(*[y == val for val in data]))
    s.add(x != y)
    s.add(x + y == 2020)
    s.add(x * y == result)

    s.check()
    return s.model()[result]


def part2():
    s = Solver()
    x, y, z, result = Ints("x y z result")

    s.add(Or(*[x == val for val in data]))
    s.add(Or(*[y == val for val in data]))
    s.add(Or(*[z == val for val in data]))
    s.add((x != y) != z)
    s.add(x + y + z == 2020)
    s.add(x * y * z == result)

    s.check()
    return s.model()[result]


print("Part 1:", part1())
print("Part 2:", part2())
