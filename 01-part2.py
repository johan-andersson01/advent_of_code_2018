import argparse
from pathlib import Path
from functools import reduce
from operator import add, sub

"""
You notice that the device repeats the same frequency change list over and over. To calibrate the device, you need to find the first frequency it reaches twice.
"""


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, default='input/01.txt', help='Path to input')
    return parser.parse_args()


def main():
    args = get_args()
    seen_freqs = {}
    freq_sum = 0
    seen_freqs[0] = 1
    freq_changes = args.input.read_text().strip().split('\n')

    while True:
        for f in freq_changes:
            op = f[0]
            change = int(f[1:])
            freq_sum = freq_sum + change if op == '+' else freq_sum - change
            if freq_sum in seen_freqs:
                print(freq_sum)
                return
            seen_freqs[freq_sum] = 1


if __name__ == "__main__":
    main()
