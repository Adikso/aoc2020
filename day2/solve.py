from aoc_utils import get_input

data = get_input(
    year=2020,
    day=2,
    lines=True,
    pattern="^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)$",
    pattern_types=[int, int, str, str]
)


def part1():
    def is_valid(policy):
        min_count, max_count, letter, password = policy

        count = 0
        for char in password:
            if char == letter:
                count += 1

        return min_count <= count <= max_count

    valid_passwords = filter(is_valid, data)
    return len(list(valid_passwords))


def part2():
    def is_valid(policy):
        pos1, pos2, letter, password = policy
        return (password[pos1 - 1] == letter) ^ (password[pos2 - 1] == letter)

    valid_passwords = filter(is_valid, data)
    return len(list(valid_passwords))


print('Part1:', part1())
print('Part2:', part2())
