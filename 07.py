import argparse
from pathlib import Path
from collections import defaultdict
from functools import reduce
from copy import deepcopy


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, default='input/07.txt', help='Path to input')
    return parser.parse_args()


def main():
    args = get_args()
    raw_instructions = map(lambda instr: instr.split(), args.input.read_text().strip().split('\n'))
    parsed_instructions = list(map(lambda instr: (instr[1], instr[-3]), raw_instructions))
    requirements = defaultdict(list)
    done     = set()

    for c in map(chr, range(ord('A'), ord('Z') + 1)):
        requirements[c] = []

    for req, instr in parsed_instructions:
        requirements[instr].append(req)

    answer = []

    todo = sorted(requirements.items(), key=lambda kv: kv[0])

    while len(todo) > 0:
       for instr, reqs in todo:
           if all(req in done for req in reqs):
               done.add(instr)
               answer.append(instr)
               del requirements[instr]
               break
       todo = sorted(requirements.items(), key=lambda kv: kv[0])
    print('part 1:', ''.join(answer))
    print('part 2: unsolved')


if __name__ == "__main__":
    main()
