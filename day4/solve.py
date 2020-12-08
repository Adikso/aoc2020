import re

from aoc_utils import get_input

data = get_input(year=2020, day=4)
passwords = [dict(re.findall(r"([a-z]{3}):([^\s]+)", x.replace("\n", " "))) for x in data.split("\n\n")]


def part1():
    valid_count = 0
    for password in passwords:
        valid_count += int({'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} <= password.keys())

    return valid_count


def part2():
    def check_number(value, min, max):
        return value.isdigit() and min <= int(value) <= max

    valid_count = 0
    for password in passwords:
        if not {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} <= password.keys():
            continue

        if 'byr' in password and not check_number(password['byr'], 1920, 2002):
            continue

        if 'iyr' in password and not check_number(password['iyr'], 2010, 2020):
            continue

        if 'eyr' in password and not check_number(password['eyr'], 2020, 2030):
            continue

        if 'hgt' in password:
            unit = password['hgt'][-2:]
            value = password['hgt'][:-2]

            if unit not in ['cm', 'in']:
                continue

            if unit == 'cm' and not check_number(value, 150, 193):
                continue

            if unit == 'in' and not check_number(value, 59, 76):
                continue

        if 'hcl' in password and not re.match(r'^#[0-9a-f]{6}$', password['hcl']):
            continue

        if 'ecl' in password and password['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            continue

        if 'pid' in password and not re.match(r'^[0-9]{9}$', password['pid']):
            continue

        valid_count += 1

    return valid_count


print("Part 1:", part1())
print("Part 2:", part2())
