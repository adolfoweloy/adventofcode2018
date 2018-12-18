import sys
import re

def first():
    size = 1000
    result = [[0 for i in range(size)] for i in range(size)]
    count = 0

    for line in sys.stdin:
        m = re.match(".*@\s(\d+),(\d+):\s(\d+)x(\d+)", line)
        left, top     = int(m.group(1)), int(m.group(2))
        width, height = int(m.group(3)), int(m.group(4))
        
        for col in range(top, top + height):
            for row in range(left, left + width): 
                if result[col][row] == 1:
                    result[col][row] = 2
                    count += 1
                elif result[col][row] == 0:
                    result[col][row] = 1
                else:
                    continue

    print(count)

if __name__ == "__main__":
    first()