import argparse
from pathlib import Path


"""
After feeling like you've been falling for a few minutes, you look at the device's tiny screen. "Error: Device must be calibrated before first use. Frequency drift detected. Cannot maintain destination lock." Below the message, the device shows a sequence of changes in frequency (your puzzle input). A value like +6 means the current frequency increases by 6; a value like -3 means the current frequency decreases by 3.
"""


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, default='input/01.txt', help='Path to input')
    return parser.parse_args()


def main():
    args = get_args()
    freq_changes = args.input.read_text().strip().replace('\n', '')
    print(eval(freq_changes))


if __name__ == "__main__":
    main()
