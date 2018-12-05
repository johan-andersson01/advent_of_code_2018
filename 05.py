import argparse
from pathlib import Path
import re


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, default='input/05.txt', help='Path to input')
    return parser.parse_args()


def lower_upper_pairs():
    lows  = range(ord('a'), ord('z') + 1)
    ups = range(ord('A'), ord('Z') + 1)
    for low, up in zip(lows, ups):
         yield map(chr, (low, up))


def solve(collapsed:str):
    prev_iter = ''
    while len(collapsed) != len(prev_iter):
        prev_iter = collapsed
        for low, up in lower_upper_pairs():
            collapsed = re.sub(low+up, '', collapsed)
            collapsed = re.sub(up+low, '', collapsed)
    return len(collapsed)


def main():
    args = get_args()
    string = args.input.read_text().strip()
    print('part 1:', solve(string))
    best_len = len(string)
    for c in set(string.lower()):
        edited = string.replace(c, '').replace(c.upper(), '')
        sol = solve(edited)
        if sol < best_len:
            best_len = sol
    print('part 2:', best_len)


if __name__ == "__main__":
    main()
