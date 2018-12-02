import argparse
from pathlib import Path
from collections import defaultdict
from itertools import product


"""
The boxes will have IDs which differ by exactly one character at the same position in both strings. What letters are common between the two correct box IDs?
"""


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, default='input/02.txt', help='Path to input')
    return parser.parse_args()


# returns the similaritys score (0 if equal) and the position of the last dissimilarity (0 if none)
def string_similarity(s1:str, s2:str):
    sim = 0
    i   = 0
    for pos, (c1, c2) in enumerate(zip(s1, s2)):
        if c1 != c2:
            sim += 1
            i = pos
    return sim, i


def main():
    args = get_args()
    boxes = args.input.read_text().strip().split('\n')
    for box1, box2 in product(boxes, boxes):
        sim, pos = string_similarity(box1, box2)
        if sim == 1:
            print(box1[:pos] + box1[pos+1:])
            return


if __name__ == "__main__":
    main()
