import re

TEST = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
"""


def digital_plumber(programs_list):
    regex = r'(?P<prog_id>\d+) <-> (?P<prog_list>.*)'
    programs = dict()

    for program_str in programs_list:
        match = re.match(regex, program_str)
        prog_id = int(match.group('prog_id'))
        prog_list = [int(x) for x in match.group('prog_list').split(',')]

        programs[prog_id] = prog_list

    group0_programs = []
    programs_to_check = []

    group0_programs.append(0)

    print()


def load_puzzle():
    f = open('day12input.txt', 'r')

    return [x.strip('\n') for x in f.readlines()]


if __name__ == '__main__':
    in_data = [x for x in (TEST.strip('\n')).split('\n')]
    # in_data = load_puzzle()

    digital_plumber(in_data)
