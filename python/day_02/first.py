from collections import defaultdict
import sys

def main():
    twos = 0
    threes = 0

    for line in sys.stdin:
        counter = defaultdict(int)

        for char in line:
            counter[char] += 1

        if 2 in counter.values():
            twos += 1

        if 3 in counter.values():
            threes += 1

    print twos * threes

if __name__ == "__main__":
    main()
