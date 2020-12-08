from aoc_utils import get_input_raw


class Node:
    def __init__(self, parents, children):
        self.parents = parents
        self.children = children


def parse():
    quick_access = {}

    with get_input_raw(2020, 7) as file:
        for line in file:
            base_parts = line.rstrip('\n.').split(" bags contain ")
            base_parts[1] = [(int(x[0]), x[2:x.rindex(' ')]) for x in base_parts[1].split(", ") if base_parts[1] != 'no other bags']
            name, contains = base_parts

            if name not in quick_access:
                quick_access[name] = Node({}, {})

            for child_count, child_name in contains:
                quick_access[name].children[child_name] = child_count

            for entry_count, entry_name in contains:
                if entry_name not in quick_access:
                    quick_access[entry_name] = Node({}, {})

                quick_access[entry_name].parents[name] = entry_count

    return quick_access


quick = parse()


def part1():
    visited = set()
    queue = [quick['shiny gold']]
    visited.add('shiny gold')

    while queue:
        entry = queue.pop(0)
        for parent in entry.parents:
            if parent not in visited:
                queue.append(quick[parent])
                visited.add(parent)

    visited.remove('shiny gold')
    return len(visited)


def part2():
    def process(entry, amount):
        result = amount
        for name, count in entry.children.items():
            result += process(quick[name], count) * amount

        return result

    total = process(quick['shiny gold'], 1) - 1
    return total


print('Part 1:', part1())
print('Part 2:', part2())
