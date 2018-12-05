import argparse
from pathlib import Path
from collections import defaultdict


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, default='input/05.txt', help='Path to input')
    return parser.parse_args()


def reacts(c1:str, c2:str):
    def is_lower(c:str):
        return c == c.lower()
    def is_upper(c:str):
        return c == c.upper()

    return c1.lower() == c2.lower() and (is_lower(c1) and is_upper(c2) or is_upper(c1) and is_lower(c2))

def solve(string:str):
    i = 0
    diff = 1 # difference between index(c1) and index(c2)
    removed = defaultdict(int)
    max_i = len(string) - 1
    while i < max_i - 1:
        c1 = string[i]
        i += 1
        while i in removed:
            diff += 1
            i += 1
        if i > max_i:
            break # everything to the right of c1 has been removed
        c2 = string[i]
        if reacts(c1, c2):
            removed[i] = 1 # c2
            i -= diff
            removed[i] = 1 # c1
            while i in removed:
                i -= 1
        diff = 1

    return len([k for k in range(len(string)) if k not in removed])


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
