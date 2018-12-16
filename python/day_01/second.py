import sys

## to avoid O(n) searches I am trading off for space usage
## so the history is maintained inside a dictionary for O(1) access

def main():
    history = {}
    sample = []
    current = 0

    ## first turn
    for line in sys.stdin:
        freq = int(line)
        current += freq
        sample.append(freq)
        history[current] = True

    ## search for repetition
    index = 0
    while True:
        current += sample[index]
        if current in history:
            print current
            break
        else:
            history[current] = True
        index = (index + 1) % len(sample)

if __name__ == "__main__":
    main()
