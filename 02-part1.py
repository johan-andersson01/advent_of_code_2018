import argparse
from pathlib import Path
from collections import defaultdict


"""
To make sure you didn't miss any, you scan the likely candidate boxes again, counting the number that have an ID containing exactly two of any letter and then separately counting those with exactly three of any letter. You can multiply those two counts together to get a rudimentary checksum and compare it to what your device predicts.
"""


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, default='input/02.txt', help='Path to input')
    return parser.parse_args()


def has_exactly_n_of_same_char(n:int, id:str):
    chars = defaultdict(int)
    for c in id:
        chars[c] += 1
    for _, count in chars.items():
        if count == n:
            return True
    return False


def main():
    args = get_args()
    boxes = args.input.read_text().strip().split('\n')

    boxes_with_3 = list(filter(lambda id: has_exactly_n_of_same_char(3, id), boxes))
    boxes_with_2 = list(filter(lambda id: has_exactly_n_of_same_char(2, id), boxes))

    print(len(boxes_with_2)*len(boxes_with_3))


if __name__ == "__main__":
    main()
