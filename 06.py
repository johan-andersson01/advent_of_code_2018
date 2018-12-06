import argparse
from pathlib import Path
from collections import defaultdict


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, default='input/06.txt', help='Path to input')
    return parser.parse_args()


def manhattan(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])


def closest_coord(coord, coords):
    closest = min(coords, key=lambda c: manhattan(coord, c))
    dist = manhattan(coord, closest)
    for c in coords:
        if c == closest:
            continue
        if manhattan(coord, c) == dist:
            return None
    return closest


def main():
    args = get_args()
    coords = args.input.read_text().strip().split('\n')
    # format coords to [{'x': int, 'y': int}]
    coords = list(map(lambda line: tuple(map(int, line.split(', '))), coords))
    min_x = min(coords, key=lambda c: c[0])
    max_x = max(coords, key=lambda c: c[0])
    min_y = min(coords, key=lambda c: c[1])
    max_y = max(coords, key=lambda c: c[1])
    border = {'x': set([min_x[0], max_x[0]]), 'y': set([min_y[1], max_y[1]])}

    grid = {}
    for x in range(min_x[0], max_x[0] + 1):
        for y in range(min_y[1], max_y[1] + 1):
            grid[(x,y)] = closest_coord((x, y), coords)

    # any coordinate with a minimal/maximal x or y value can be disregarded since its
    # area will be infinite
    area = defaultdict(int)
    for _, closest in grid.items():
        if closest != None and closest[0] not in border['x'] and closest[1] not in border['y']:
            area[closest] += 1

    max_area_coord = max(area, key=area.get)
    print('part 1:', area[max_area_coord])

    safe = 0
    for x in range(min_x[0], max_x[0] + 1):
        for y in range(min_y[1], max_y[1] + 1):
            dist_sum = 0
            for coord in coords:
                dist_sum += manhattan((x, y), coord)
            if dist_sum < 10000:
                safe += 1

    print('part 2:', safe)

if __name__ == "__main__":
    main()
