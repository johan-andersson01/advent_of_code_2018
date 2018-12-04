import argparse
from pathlib import Path
from collections import defaultdict
import re


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, default='input/04.txt', help='Path to input')
    return parser.parse_args()


def main():
    args = get_args()
    guards = defaultdict(dict)
    rows = args.input.read_text().strip().split('\n')
    rows.sort()
    # map row -> {time: hh:mm, desc: str}
    rows = iter(map(lambda row: {'time':row.split('] ')[0].split(' ')[1], 'desc': row.split('] ')[1]}, rows))

    guard_id  = None
    asleep_at = -1
    awake_at  = -1
    while True:
        try:
            row = next(rows)
        except StopIteration:
            break
        # parse guard
        if row['desc'][0] == 'G':
            guard_id = int(re.sub('[a-zA-Z# ]+', '', row['desc']))
            if guard_id not in guards:
                guards[guard_id] = {'total': 0, 'mins': defaultdict(int)}
        # parse fall asleep
        elif row['desc'][0] == 'f':
            asleep_at = int(row['time'][3:])
        # parse awake from sleep
        elif row['desc'][0] == 'w':
            awake_at = int(row['time'][3:])
            for minute in range(asleep_at, awake_at):
                guards[guard_id]['mins'][minute] += 1
                guards[guard_id]['total'] += 1
        else:
            raise Exception

    # strategy 1
    sleepiest_guard  = max(guards.items(), key=(lambda g: g[1]['total']))
    sleepiest_minute = max(sleepiest_guard[1]['mins'].items(), key=(lambda m: m[1]))
    print('part 1: ', sleepiest_guard[0] * sleepiest_minute[0])

    # strategy 2
    def most_freq_minute(minutes):
        return 0 if len(minutes) == 0 else max(minutes)

    sleepiest_guard  = max(guards.items(), key=(lambda g: most_freq_minute(g[1]['mins'].values())))
    sleepiest_minute = max(sleepiest_guard[1]['mins'].items(), key=(lambda m: m[1]))
    print('part 2: ', sleepiest_guard[0] * sleepiest_minute[0])


if __name__ == "__main__":
    main()
