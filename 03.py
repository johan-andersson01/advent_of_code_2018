import argparse
from pathlib import Path
from collections import defaultdict


"""
To make sure you didn't miss any, you scan the likely candidate boxes again, counting the number that have an ID containing exactly two of any letter and then separately counting those with exactly three of any letter. You can multiply those two counts together to get a rudimentary checksum and compare it to what your device predicts.
"""


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, default='input/03.txt', help='Path to input')
    return parser.parse_args()


def add_claim(cloth:dict, claim:dict):
    overlaps = 0
    for x in range(claim['left'], claim['left']+claim['wide']):
        for y in range(claim['top'], claim['top']+claim['long']):
            if (x,y) in cloth:
                if cloth[(x,y)] == 1:
                    overlaps += 1
            cloth[(x,y)] += 1
    return overlaps


def find_no_overlap(cloth:dict, claim:dict):
    overlaps = 0
    for x in range(claim['left'], claim['left']+claim['wide']):
        for y in range(claim['top'], claim['top']+claim['long']):
            if (x,y) in cloth and cloth[(x,y)] > 1:
                overlaps += 1
    return claim['id'], overlaps
        

def main():
    args = get_args()
    rows = args.input.read_text().strip().split('\n')
    cloth = defaultdict(int)
    overlaps = 0
    claims = []
    for row in rows:
        row = [row.split()[0][1:]] + row.split()[2:]
        dists = row[1].split(',')
        claim = {'left': int(dists[0]), 'top': int(dists[1][:-1])}
        measures = list(map(int, row[2].split('x')))
        claim = dict(claim, **{'id': int(row[0]), 'wide': measures[0], 'long': measures[1]})
        claims.append(claim)
        overlaps += add_claim(cloth, claim)
    print('part 1:', overlaps)
    for claim in claims:
        id, overlaps = find_no_overlap(cloth, claim)
        if overlaps == 0:
            print('part 2:', id)
            return

if __name__ == "__main__":
    main()
