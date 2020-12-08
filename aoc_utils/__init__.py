import re
from pathlib import Path

import requests
import os.path
import os

from dotenv import load_dotenv
load_dotenv(dotenv_path=Path(os.path.dirname(os.path.realpath(__file__))) / '.env')

BASE_URL = 'https://adventofcode.com'


def get_input_raw(year, day, filename="input.txt"):
    if not os.path.exists(filename):
        r = requests.get(f'{BASE_URL}/{year}/day/{day}/input', cookies={
            "session": os.getenv('session')
        })

        with open(filename, 'wb') as file:
            file.write(r.content)

    return open(filename, 'r')


def get_input(year, day, lines=False, numbers=False, pattern=None, pattern_types=None, filename="input.txt"):
    with get_input_raw(year, day, filename) as file:
        if lines:
            content = [x.strip() for x in file.readlines()]
        else:
            content = file.read()

    if lines and numbers:
        content = [int(x) for x in content]

    if lines and pattern:
        converted = []
        for x in content:
            match = re.match(pattern, x)
            values = match.groups()
            if pattern_types:
                values = tuple([pattern_types[i](x) for i, x in enumerate(values)])
            converted.append(values)

        content = converted

    return content
