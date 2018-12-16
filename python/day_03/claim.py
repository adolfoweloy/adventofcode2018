class Claim(object):
    def __init__(self, claim_id, coordinates, dimension):
        self._claim_id = claim_id
        self._coordinates = coordinates
        self._dimension = dimension

    @property
    def coordinates(self):
        return self._coordinates

    @property
    def dimension(self):
        return self._dimension

    def square_inches(self):
        return self._dimension[0] * self._dimension[1]

    def get_overlaped_area(self, claim):
        x1 = claim.coordinates[0]
        x2 = claim.coordinates[0] + claim.dimension[0]

        xint = self.get_line_intersection(x1, x2, self.xline())
        if isinstance(xint, tuple):
            y1 = claim.coordinates[1]
            y2 = claim.coordinates[1] + claim.dimension[1]
            yint = self.get_line_intersection(y1, y2, self.yline())
            if isinstance(yint, tuple):
                return self._create_rectangle(xint, yint)

        return None

    def _create_rectangle(self, xline, yline):
        coordinates = (xline[0], yline[0])
        dimension = (xline[1] - xline[0], yline[1] - yline[0])
        return Claim(0, coordinates, dimension)

    def get_line_intersection(self, p1, p2, line):
        p1_overlaps = p1 in range(line[0], line[1] + 1)
        p2_overlaps = p2 in range(line[0], line[1] + 1)
        if p1_overlaps and p2_overlaps:
            return (p1, p2)
        if p1_overlaps and not p2_overlaps:
            return (p1, line[1])
        if not p1_overlaps and p2_overlaps:
            return (line[0], p2)
        return None

    def xline(self):
        return (self._coordinates[0], self._dimension[0] + self._coordinates[0])

    def yline(self):
        return (self._coordinates[1], self._dimension[1] + self._coordinates[1])

    @staticmethod
    def get_claim(content):
        tokens = content.split(' ')
        claim_id = tokens[0][1:]
        coordinates = tuple([int(x) for x in tokens[2][:-1].split(',')])
        dimension = tuple([int(x) for x in tokens[3].strip().split('x')])
        return Claim(claim_id, coordinates, dimension)

    def __eq__(self, other):
        return self._coordinates == other.coordinates and self.dimension == self.dimension

    def __hash__(self):
        return self._coordinates.__hash__() + self._dimension.__hash__()

    def __str__(self):
        return "{claim_id: %s, coordinates: %s, dimension: %s}" % (
            self._claim_id,
            self._coordinates,
            self._dimension)

