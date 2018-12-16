import sys
from claim import Claim

def main():
    claims = set()
    overlaps = set()
    sqrt_inches = 0

    for line in sys.stdin:
        new_claim = Claim.get_claim(line)
        for claim in claims:
            overlaping = claim.get_overlaped_area(new_claim)
            if isinstance(overlaping, Claim):
                overlaps.add(overlaping)
        claims.add(new_claim)

    for overlap in overlaps:
        sqrt_inches += overlap.square_inches()

    diff = 0
    while True:
        if len(overlaps) == 0:
            break
        tmp = overlaps.pop()
        for overlap in overlaps:
            found = overlap.get_overlaped_area(tmp)
            if isinstance(found, Claim):
                diff += found.square_inches()

    print(sqrt_inches)
    print(diff)
    print(sqrt_inches - diff)

if __name__ == "__main__":
    main()

