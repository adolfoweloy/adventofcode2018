from collections import defaultdict
import sys

## finds letters that appears twice (doesnt count if more twices)
## finds letters that appears three (doesnt count if more threes)
## multiplies the number of words with twices times words with threes
def first():
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

## finds a word built up of two words that differs by 1 char
## when 2 words diffs by 1 char, a new word with the remaining char is created.
def second():
    words = []
    wfound = None

    # brute force
    for line in sys.stdin:
        for word in words:
            tmp = []
            for i, c in enumerate(line):
                if c == word[i]:
                    tmp.append(c)
            if len(word) - len(tmp) == 1:
                wfound = str.join("", tmp)
                break
        words.append(line)

    print(wfound)

if __name__ == "__main__":
    first()
