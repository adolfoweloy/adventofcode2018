import sys

def main():
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
    main()
