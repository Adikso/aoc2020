from time import perf_counter

from aoc_utils import get_input
from functools import partial, reduce

data = get_input(year=2020, day=6)
groups = [x.splitlines() for x in data.split('\n\n')]


def process(func):
    return sum((len(reduce(lambda a, b: func(set(a), set(b)), g)) for g in groups))


print('Part 1:', process(set.union))
print('Part 2:', process(set.intersection))
