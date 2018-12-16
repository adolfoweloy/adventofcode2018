import sys

def main():
    result = 0
    for line in sys.stdin:
        result += int(line)
    print result

if __name__ == "__main__":
    main()
