import sys

def first():
    result = 0
    for line in sys.stdin:
        result += int(line)
    print result

def second():
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
    first()
